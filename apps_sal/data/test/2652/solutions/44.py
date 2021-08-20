import sys
sys.setrecursionlimit(10 ** 5)
n = int(input())
xy = []
for i in range(n):
    (x, y) = map(int, input().split())
    xy.append((i, x, y))
xx = sorted(xy, key=lambda x: x[1])
yy = sorted(xy, key=lambda x: x[2])
li = []
for i in range(n - 1):
    li.append((xx[i][0], xx[i + 1][0], xx[i + 1][1] - xx[i][1]))
    li.append((yy[i][0], yy[i + 1][0], yy[i + 1][2] - yy[i][2]))
li.sort(key=lambda x: x[2])


class UnionFind:

    def __init__(self, li):
        self.li = li

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


uf = UnionFind(list(range(n)))
ans = 0
for (x, y, cost) in li:
    if uf.same(x, y):
        continue
    uf.unite(x, y)
    ans += cost
print(ans)
