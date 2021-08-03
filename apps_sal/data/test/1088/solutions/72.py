import numpy as np


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

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}


mod = 998244353
n, k = map(int, input().split())
a = np.array([list(map(int, input().split())) for _ in range(n)], dtype=np.int64)
ans = 1
for _ in range(2):
    uf = UnionFind(n)
    for i in range(n):
        for j in range(i, n):
            if i == j:
                continue
            if max(a[i] + a[j]) <= k:
                uf.union(i, j)
    c = uf.all_group_members()
    for key, v in c.items():
        tmp = 1
        for i in range(len(v)):
            tmp *= i + 1
            tmp %= mod
        ans *= tmp
        ans %= mod
    a = a[::-1].T
print(ans)
