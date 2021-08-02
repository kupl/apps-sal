import sys

sys.setrecursionlimit(10**5)


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def root(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.root(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return
        if self.parents[x] > self.parents[y]:
            rx, ry = ry, rx
        self.parents[rx] += self.parents[ry]
        self.parents[ry] = rx

    def same(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        return rx == ry

    def size(self, x):
        return -self.parents[self.root(x)]


n, m = list(map(int, input().split()))
bridges = [tuple((int(i) - 1 for i in input().split())) for _ in range(m)]
islands = UnionFind(n)
res = [n * (n - 1) // 2]
for a, b in bridges[:0:-1]:
    if islands.same(a, b):
        res.append(res[-1])
    else:
        res.append(res[-1] - islands.size(a) * islands.size(b))
        islands.unite(a, b)
print(('\n'.join(map(str, res[::-1]))))
