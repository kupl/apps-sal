class UnionFind:
    def __init__(self, N):
        self.N = N

        self.parent = [-1] * N

    def root(self, i):
        if self.parent[i] < 0:
            return i

        r = self.root(self.parent[i])
        self.parent[i] = r
        return r

    def unite(self, i, j):
        i = self.root(i)
        j = self.root(j)

        if i == j:
            return

        if i > j:
            i, j = j, i

        self.parent[i] += self.parent[j]
        self.parent[j] = i

    def same(self, i, j):
        return self.root(i) == self.root(j)

    def size(self, i):
        return -self.parent[self.root(i)]

    def roots(self):
        return [self.root(i) for i in range(self.N)]


N, K, L = map(int, input().split())

road = UnionFind(N)
rail = UnionFind(N)

for _ in range(K):
    p, q = map(int, input().split())
    p += -1
    q += -1
    road.unite(p, q)

for _ in range(L):
    r, s = map(int, input().split())
    r += -1
    s += -1
    rail.unite(r, s)

pair = {}
for i, j in zip(road.roots(), rail.roots()):
    t = (i, j)

    if t in pair:
        pair[t] += 1
    else:
        pair[t] = 1

ans = ' '.join([str(pair[(i, j)]) for i, j in zip(road.roots(), rail.roots())])
print(ans)
