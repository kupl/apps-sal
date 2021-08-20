from collections import defaultdict


class UnionFind:

    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            (x, y) = (y, x)
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -size.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for (i, x) in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}


(n, k, l) = map(int, input().split())
uf1 = UnionFind(n)
for _ in range(k):
    (u, v) = map(int, input().split())
    uf1.unite(u - 1, v - 1)
uf2 = UnionFind(n)
for _ in range(l):
    (u, v) = map(int, input().split())
    uf2.unite(u - 1, v - 1)
d = defaultdict(int)
for i in range(n):
    d[uf1.find(i), uf2.find(i)] += 1
ans = [d[uf1.find(i), uf2.find(i)] for i in range(n)]
print(*ans)
