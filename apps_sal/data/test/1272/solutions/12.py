

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
            u, v = v, u

        self.parents[u] += self.parents[v]
        self.parents[v] = u

    def size(self, v):
        return -self.parents[self.find(v)]

    def same(self, u, v):
        return self.find(u) == self.find(v)


N, M = list(map(int, input().split()))
uf = UnionFind(N)
edges = []

for i in range(M):
    A, B = list(map(int, input().split()))
    edges.append((A - 1, B - 1))


total = [N * (N - 1) // 2 for _ in range(M)]

for i in range(M - 1):
    u, v = edges[-i - 1]
    if uf.same(u, v):
        total[-i - 2] = total[-i - 1]
    else:
        total[-i - 2] = total[-i - 1] - uf.size(u) * uf.size(v)
        uf.unite(u, v)

for t in total:
    print(t)
