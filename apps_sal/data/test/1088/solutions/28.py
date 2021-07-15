class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [-1] * n

    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.par[x] > self.par[y]:
            x, y = y, x

        self.par[x] += self.par[y]
        self.par[y] = x

    def size(self, x):
        return -self.par[self.find(x)]

n,k=list(map(int,input().split()))
A=[list(map(int, input().split())) for _ in range(n)]

uf1=UnionFind(n)
uf2=UnionFind(n)

mod=998244353

fct=[1]
for i in range(1,101):
    fct.append(fct[-1]*i%mod)

for i in range(n - 1):
    for j in range(i + 1, n):
        if all(A[c][i] + A[c][j] <= k for c in range(n)):
            uf1.unite(i, j)
        if all(A[i][c] + A[j][c] <= k for c in range(n)):
            uf2.unite(i, j)
ans = 1
for i in range(n):
    if uf1.par[i] < 0:
        ans *= fct[-uf1.par[i]]
        ans %= mod
    if uf2.par[i] < 0:
        ans *= fct[-uf2.par[i]]
        ans %= mod
print(ans)



