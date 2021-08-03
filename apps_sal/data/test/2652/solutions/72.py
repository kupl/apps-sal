from operator import itemgetter


class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * n
        self.size = [1] * n

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return

        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.size[y] += self.size[x]
        else:
            self.par[y] = x
            self.size[x] += self.size[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same(self, x, y):
        if self.find(x) == self.find(y):
            return True
        else:
            return False


def kruskal(n, edges):
    uf = UnionFind(n)
    edges.sort()
    res = 0
    for d, s, t in edges:
        if not uf.same(s, t):
            uf.unite(s, t)
            res += d
    return res


n = int(input())

xy = [[i] + list(map(int, input().split())) for i in range(n)]

edges = set()
for key in [itemgetter(1), itemgetter(2)]:
    xy.sort(key=key)
    for i in range(n - 1):
        i1, x1, y1 = xy[i]
        i2, x2, y2 = xy[i + 1]
        d = min(abs(x1 - x2), abs(y1 - y2))
        edges.add((d, i1, i2))

edges = list(edges)
print((kruskal(n, edges)))
