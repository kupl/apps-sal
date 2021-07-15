# 半分全列挙バージョン
import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def allptn(abc,ma,mb):
    inf=10**9
    # a,b,cの全組合せを作る
    allabc=[(0,0,0)]
    for a,b,c in abc:
        n=len(allabc)
        for i in range(n):
            aa,bb,cc=allabc[i]
            allabc.append((aa+a,bb+b,cc+c))
    # 指標とコストの組合せにする
    # 指標が重複するときはコストが小さいほうだけ残す
    # 指標が0のときは前後半で組み合わせる必要がないので単独で答えを出しておく
    vc={}
    ans=inf
    for a,b,c in allabc[1:]:
        val=a*mb-b*ma
        if val:
            pc=vc.setdefault(val,inf)
            if c<pc:vc[val]=c
        else:
            if c<ans:ans=c
    res=[(val,c) for val,c in sorted(vc.items())]
    return ans,res

def main():
    n,ma,mb=MI()
    abc=[LI() for _ in range(n)]
    inf=10**9
    # 前半の要素をa1,b1、後半の要素をa2,b2とする
    # (a1+a2):(b1+b2)=ma:mbとなればよい。式変形すると
    # (mb*a1-ma*b1)+(mb*a2-ma*b2)=0となる
    # つまり各要素についてmb*a-ma*bという指標を計算し、前半と後半で和が0になる組合せを探せばよい
    # 前半全列挙
    ans,pre=allptn(abc[:n//2],ma,mb)
    # 後半全列挙
    ret,pos=allptn(abc[n//2:],ma,mb)
    ans=min(ans,ret)
    # 指標が昇順になるよう並び替えて、前半は前から後半は後からしゃくとり法で
    # 指標の和が0になるところのコストを求める
    j=len(pos)-1
    for val,c in pre:
        while val+pos[j][0]>0 and j:j-=1
        if val+pos[j][0]==0:ans=min(ans,c+pos[j][1])
    if ans==inf:print(-1)
    else:print(ans)

main()
