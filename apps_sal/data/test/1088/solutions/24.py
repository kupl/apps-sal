from collections import defaultdict
import math
import numpy as np
(n, k) = map(int, input().split())
a_lists = [list(map(int, input().split())) for _ in range(n)]
mod = 998244353
a_lists = np.array(a_lists)


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

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join((f'{r}: {m}' for (r, m) in self.all_group_members().items()))


def count_point(np_array):
    uf = UnionFind(n)
    for i in range(n):
        a = np_array[i]
        for j in range(i, n):
            b = np_array[j]
            if np.count_nonzero(a + b <= k) == n:
                uf.union(i, j)
    point = 1
    for (i, j) in uf.all_group_members().items():
        point *= math.factorial(len(j))
        point %= mod
    return point


ans = count_point(a_lists)
a_lists_T = a_lists.T
ans *= count_point(a_lists_T)
ans %= mod
print(ans)
