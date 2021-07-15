import sys
mod=10**9+7 ; inf=float("inf")
from math import sqrt, ceil
from collections import deque, Counter, defaultdict #すべてのkeyが用意されてる defaultdict(int)で初期化
input=lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(11451419)
from decimal import ROUND_HALF_UP,Decimal  #変換後の末尾桁を0や0.01で指定
  #Decimal((str(0.5)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
from functools import lru_cache
from bisect import bisect_left as bileft, bisect_right as biright
#メモ化再帰defの冒頭に毎回 @lru_cache(maxsize=10**10)
#引数にlistはだめ
#######ここまでテンプレ#######
#ソート、"a"+"b"、再帰ならPython3の方がいい
#######ここから天ぷら########
class UnionFind():
    def __init__(self,num):
        self.n = num         #class内変数nに、外部から入力した値numを代入
        self.parents = [-1 for i in range(self.n)]
          #parentsは要素の親(1こ上のやつ)番号0~n-1を格納、自分が最親なら-(要素数)を格納(初期値は-1)

    #xの最親は誰？
    def find(self,x):
        if self.parents[x]<0:
            return x
        else:
            self.parents[x]=self.find(self.parents[x]) #再帰して1番上までいってる
                #調べながらparentsの値を更新してる！（経路圧縮）
            return self.parents[x]

    #結合せよ
    #xの親とyの親をくっつける
    def union(self,x,y):
        xx=self.find(x)  #xxはxの最親
        yy=self.find(y)  #yyはyの最親
        if xx==yy:
            return     #同じ屋根の下にあった場合は何もしない
        else:
            size_xx=abs(self.parents[xx]) #xが含まれる木のサイズ
            size_yy=abs(self.parents[yy]) #yが含まれる木のサイズ
            if size_xx>size_yy:
                xx,yy=yy,xx  #yyの方が大きい木、ってことにする

            self.parents[yy]+=self.parents[xx] #大きい木のサイズ更新
            self.parents[xx]=yy   #サイズが小さい木を大きい木に接ぐ

    #xの属する木の大きさ（まあunionでも使ったけど）
    def size(self,x):
        xx=self.find(x)
        return abs(self.parents[xx])

    #xとyはこの空の続く場所にいますか　いつものように笑顔でいてくれますか　今はただそれを願い続ける
    def same(self,x,y):
        return 1 if self.find(x)==self.find(y) else 0

    #xと　同じ木にいる　メンバーは？
    def members(self,x):
        xx=self.find(x)
        return [i for i in range(self.n) if self.find(i)==xx]
             #ifの条件式に漏れたら無視

    #最親だけを並べあげる
    def roots(self):
        return [i for i,x in enumerate(self.parents) if x < 0]
        #いやこれは天才すぎる、basisのenumerate.py参照

    #すべての最親について、メンバーを辞書で
    def all_group_members(self):
        return {r:self.members(r) for r in self.roots()}

    #グループ分けどうなりましたか、２重リストで
    def state_grouping(self):
        return list(self.all_group_members().values())

n,k,l=map(int,input().split())
uf=UnionFind(n)
uf2=UnionFind(n)
for i in range(k):
    p,q=map(int,input().split())
    p-=1;q-=1
    uf.union(p,q)
for i in range(l):
    p,q=map(int,input().split())
    p-=1;q-=1
    if 1:
        uf2.union(p,q)

C= Counter( [ ( uf.find(i),uf2.find(i) ) for i in range(n)] )
ANS=[0]*n 
for i in range(n):
    ANS[i]= C[(uf.find(i),uf2.find(i))]
print(*ANS)
