class Uf:

    def __init__(self, N):
        self.p = list(range(N))
        self.rank = [0] * N
        self.size = [1] * N

    def root(self, x):
        if self.p[x] != x:
            self.p[x] = self.root(self.p[x])
        return self.p[x]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        u = self.root(x)
        v = self.root(y)
        if u == v:
            return
        if self.rank[u] < self.rank[v]:
            self.p[u] = v
            self.size[v] += self.size[u]
            self.size[u] = 0
        else:
            self.p[v] = u
            self.size[u] += self.size[v]
            self.size[v] = 0
            if self.rank[u] == self.rank[v]:
                self.rank[u] += 1

    def count(self, x):
        return self.size[self.root(x)]


(N, M, K) = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(M)]
CD = [list(map(int, input().split())) for _ in range(K)]
uf = Uf(N + 1)
M = [-1] * (N + 1)
for (a, b) in AB:
    uf.unite(a, b)
    M[a] -= 1
    M[b] -= 1
for (c, d) in CD:
    if uf.same(c, d):
        M[c] -= 1
        M[d] -= 1
for i in range(1, N + 1):
    M[i] += uf.count(i)
print(' '.join(map(str, M[1:])))
