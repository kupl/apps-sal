import sys
sys.setrecursionlimit(1500)


class UnionFind:

    def __init__(self, N):
        self.par = [-1 for i in range(N)]

    def root(self, x):
        if self.par[x] == x:
            return x
        elif self.par[x] < 0:
            return x
        else:
            par = self.root(self.par[x])
            self.par[x] = par
            return par

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        if self.par[x] > self.par[y]:
            (x, y) = (y, x)
        self.par[x] += self.par[y]
        self.par[y] = x
        return True

    def same(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        return rx == ry

    def size(self, x):
        return -self.par[self.root(x)]


(N, M) = list(map(int, input().split()))
uf = UnionFind(N)
for _ in range(M):
    (A, B) = [int(x) - 1 for x in input().split()]
    uf.unite(A, B)
print(-min(uf.par))
