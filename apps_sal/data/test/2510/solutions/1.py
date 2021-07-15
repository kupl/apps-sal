class UnionFind():
    # 作りたい要素数nで初期化
    # 使用するインスタンス変数の初期化
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
    # ノードxのrootノードを見つける
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
    # 木の併合、入力は併合したい各ノード⇒(a,b)
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
    # ノードxが属する木のサイズを返す
        return -self.parents[self.find(x)]

    def same(self, x, y):
    # 入力ノード(x,y)が同じグループに属するかを返す
        return self.find(x) == self.find(y)

    def members(self, x):
    #ノードxが属するメンバーをリスト形式で返す
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
    #親全てをリスト形式で返す
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
    #グループ数の合計を返す
        return len(self.roots())

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline



import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n,m=list(map(int,input().split()))
u=UnionFind(n)
for i in range(m):
    a,b=list(map(int,input().split()))
    a-=1
    b-=1
    u.unite(a,b)
ans=0
for i in range(n):
    ans=max(ans,u.size(i))
print(ans)

