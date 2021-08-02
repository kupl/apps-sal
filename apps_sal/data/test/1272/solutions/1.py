import math
from collections import deque


class UnionFind():
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
            x, y = y, x

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
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


def combinations_count(n, r):
    if n <= 1:
        return 0
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


n, m = map(int, input().split())
ms = [list(map(int, input().split())) for _ in range(m)]
ms.reverse()
combs = combinations_count(n, 2)
res = deque([combs])
uf = UnionFind(n)
for i in ms[:-1]:
    if not (uf.same(i[0] - 1, i[1] - 1)):
        combs -= uf.size(i[0] - 1) * uf.size(i[1] - 1)
    res.appendleft(combs)
    uf.union(i[0] - 1, i[1] - 1)
for i in res:
    print(i)
