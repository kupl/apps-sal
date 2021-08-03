N, M, K = list(map(int, input().split()))


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return
        if self.size[x] > self.size[y]:
            x, y = y, x
        self.par[x] = y
        self.size[y] += self.size[x]


uf = UnionFind(N)
fri = []
rst = [0] * N

for m in range(M):
    A, B = list(map(int, input().split()))
    A -= 1
    B -= 1
    fri.append((A, B))
    uf.unite(A, B)

for i in range(N):
    ind = uf.find(i)
    rst[i] = uf.size[ind] - 1

for f in fri:
    A, B = f
    if uf.par[A] == uf.par[B]:
        rst[A] -= 1
        rst[B] -= 1

for k in range(K):
    C, D = list(map(int, input().split()))
    C -= 1
    D -= 1
    if uf.par[C] == uf.par[D]:
        rst[C] -= 1
        rst[D] -= 1

print((" ".join(map(str, rst))))
