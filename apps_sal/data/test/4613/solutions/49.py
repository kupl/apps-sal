class UnionFind:

    def __init__(self, N):
        self.par = [-1] * N

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        if self.par[x] > self.par[y]:
            (x, y) = (y, x)
        self.par[x] += self.par[y]
        self.par[y] = x
        return True

    def root(self, x):
        if self.par[x] < 0:
            return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]

    def size(self, x):
        return -self.par[self.root(x)]


(N, M) = map(int, input().split())
Edge = []
for _ in range(M):
    (u, v) = map(int, input().split())
    Edge.append((u - 1, v - 1))
ans = 0
for e in Edge:
    uf = UnionFind(N)
    for _e in Edge:
        if e == _e:
            continue
        uf.unite(_e[0], _e[1])
    if uf.size(0) != N:
        ans += 1
print(ans)
