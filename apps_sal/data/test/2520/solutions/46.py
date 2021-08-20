class UnionFind:

    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, v):
        if self.parents[v] < 0:
            return v
        else:
            self.parents[v] = self.find(self.parents[v])
            return self.parents[v]

    def unite(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u == v:
            return
        if self.parents[u] > self.parents[v]:
            (u, v) = (v, u)
        self.parents[u] += self.parents[v]
        self.parents[v] = u

    def size(self, v):
        return -self.parents[self.find(v)]

    def same(self, u, v):
        return self.find(u) == self.find(v)


(N, M, K) = map(int, input().split())
uf = UnionFind(N + 1)
F = [0] * (N + 1)
B = [0] * (N + 1)
for _ in range(M):
    (a, b) = map(int, input().split())
    uf.unite(a, b)
    F[a] += 1
    F[b] += 1
for _ in range(K):
    (c, d) = map(int, input().split())
    if uf.same(c, d):
        B[c] += 1
        B[d] += 1
for i in range(1, N + 1):
    ans = uf.size(i) - F[i] - B[i] - 1
    print(ans, end=' ')
print()
