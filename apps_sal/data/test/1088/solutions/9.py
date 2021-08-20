import numpy as np


class UnionFind(object):

    def __init__(self, n=1):
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, x):
        """
        x が属するグループを探索して親を出す。
        """
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        """
        x と y のグループを結合
        """
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                (x, y) = (y, x)
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.par[y] = x
            self.size[x] += self.size[y]

    def is_same(self, x, y):
        """
        x と y が同じグループか否か
        """
        return self.find(x) == self.find(y)

    def get_size(self, x):
        """
        x が属するグループの要素数
        """
        x = self.find(x)
        return self.size[x]


(N, K) = map(int, input().split())
MOD = 998244353
fac = [-1] * (N + 1)
fac[0] = 1
fac[1] = 1
finv = [-1] * (N + 1)
finv[0] = 1
finv[1] = 1
inv = [-1] * (N + 1)
inv[0] = 0
inv[1] = 1
for i in range(2, N + 1):
    fac[i] = fac[i - 1] * i % MOD
    inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
    finv[i] = finv[i - 1] * inv[i] % MOD
A = np.array([list(map(int, input().split())) for _ in range(N)])
uf0 = UnionFind(N)
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        for k in range(N):
            if A[i, k] + A[j, k] > K:
                break
        else:
            uf0.union(i, j)
par0 = set([])
for i in range(N):
    par = uf0.find(i)
    par0.add(par)
X = 1
for x in par0:
    temp = uf0.get_size(x)
    X = X * fac[temp] % MOD
A = A.T
uf1 = UnionFind(N)
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        for k in range(N):
            if A[i, k] + A[j, k] > K:
                break
        else:
            uf1.union(i, j)
par1 = set([])
for i in range(N):
    par = uf1.find(i)
    par1.add(par)
Y = 1
for y in par1:
    temp = uf1.get_size(y)
    Y = Y * fac[temp] % MOD
ans = X * Y % MOD
print(ans)
