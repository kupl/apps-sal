import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
xy = []
for _ in range(m):
    x, y, _ = map(int, input().split())
    xy.append((x - 1, y - 1))


class UnionFind():
    def __init__(self, n):
        self.li = list(range(n))

    def root(self, x):
        if self.li[x] == x:
            return x
        self.li[x] = self.root(self.li[x])
        return self.li[x]

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return
        self.li[ry] = rx

    def same(self, x, y):
        return self.root(x) == self.root(y)


uf = UnionFind(n)
for x, y in xy:
    uf.unite(x, y)
for i in range(n):
    uf.root(i)
print(len(set(uf.li)))
