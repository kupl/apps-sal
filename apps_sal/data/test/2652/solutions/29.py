import sys
input = sys.stdin.readline
N = int(input())
XY = [tuple(map(int, input().split() + [i])) for i in range(N)]


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
            (ra, rb) = (rb, ra)
        self._size[ra] += self._size[rb]
        self.parent[rb] = ra
        self.count += 1

    def size(self, a):
        return self._size[self.root(a)]


uf = UnionFind(N)
sx = sorted(XY, key=lambda x: x[0])
sy = sorted(XY, key=lambda x: x[1])
es = []
for ((x1, _, i), (x2, _, j)) in zip(sx, sx[1:]):
    es.append((x2 - x1, i, j))
for ((_, y1, i), (_, y2, j)) in zip(sy, sy[1:]):
    es.append((y2 - y1, i, j))
es.sort(key=lambda x: x[0])
ans = 0
for (d, i, j) in es:
    if uf.is_same(i, j):
        continue
    uf.unite(i, j)
    ans += d
print(ans)
