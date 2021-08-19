(N, M) = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(M)]


class UnionFind(object):

    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            (x, y) = (y, x)
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for (i, x) in enumerate(self.parents) if x < 0]


uf = UnionFind(N)
for (a, b) in AB:
    uf.union(a - 1, b - 1)
max_ = 0
roots = uf.roots()
for r in roots:
    max_ = max(max_, uf.size(r))
print(max_)
