import numpy as np
from collections import defaultdict


class UnionFind(object):
    def __init__(self, n):
        self.n = n
        self.root = [-1] * n

    def find(self, x):
        if self.root[x] < 0:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.root[x] > self.root[y]:
            x, y = y, x
        self.root[x] += self.root[y]
        self.root[y] = x
        return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return self.root[self.find(x)] * -1

    def get_all_groups(self):
        all_groups = defaultdict(list)
        for i in range(self.n):
            all_groups[self.find(i)].append(i)
        return dict(all_groups)


n, m = map(int, input().split())
a = np.array(list(map(int, input().split())))
b = np.array(list(map(int, input().split())))

uf = UnionFind(n)
for _ in range(m):
    c, d = map(int, input().split())
    uf.unite(c - 1, d - 1)

for i in uf.get_all_groups().values():
    if a[i].sum() != b[i].sum():
        print('No')
        return

print('Yes')
