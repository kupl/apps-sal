N, M, *X = list(map(int, open(0).read().split()))


class UnionFind:
    def __init__(self, n=0):
        self.d = [-1] * n
        self.u = n

    def root(self, x):
        if self.d[x] < 0:
            return x
        self.d[x] = self.root(self.d[x])
        return self.d[x]

    def unite(self, x, y):
        x, y = self.root(x), self.root(y)
        if x == y:
            return False
        if x > y:
            x, y = y, x
        self.d[x] += self.d[y]
        self.d[y] = x
        self.u -= 1
        return True

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def size(self, x):
        return -self.d[self.root(x)]

    def num_union(self):
        return self.u


u = UnionFind(N)
for x, y, z in zip(*[iter(X)] * 3):
    u.unite(x - 1, y - 1)
print((u.num_union()))
