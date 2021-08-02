N = int(input())
XYI = [tuple(map(int, input().split() + [i])) for i in range(N)]
sx = sorted(XYI, key=lambda x: x[0])
sy = sorted(XYI, key=lambda x: x[1])

es = []
for (x0, _, i0), (x1, _, i1) in zip(sx, sx[1:]):
    es.append((x1 - x0, i0, i1))
for (_, y0, i0), (_, y1, i1) in zip(sy, sy[1:]):
    es.append((y1 - y0, i0, i1))
es.sort(key=lambda x: x[0])


class UnionFind:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self._size = [1] * N
        self.count = 0

    def root(self, a):
        if self.parent[a] == a:
            return a
        else:
            self.parent[a] = self.root(self.parent[a])
            return self.parent[a]

    def is_same(self, a, b):
        return self.root(a) == self.root(b)

    def unite(self, a, b):
        ra = self.root(a)
        rb = self.root(b)
        if ra == rb:
            return
        if self._size[ra] < self._size[rb]:
            ra, rb = rb, ra
        self._size[ra] += self._size[rb]
        self.parent[rb] = ra
        self.count += 1

    def size(self, a):
        return self._size[self.root(a)]


uf = UnionFind(N)
ans = 0
for d, a, b in es:
    if uf.is_same(a, b):
        continue
    uf.unite(a, b)
    ans += d
print(ans)
