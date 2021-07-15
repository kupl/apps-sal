import sys
from collections import deque, defaultdict, Counter
from itertools import accumulate, product, permutations, combinations
from operator import itemgetter
from bisect import bisect_left, bisect_right
from heapq import heappop, heappush
from math import ceil, floor, sqrt, gcd, inf
from copy import deepcopy
import numpy as np
import scipy as sp

INF = inf
MOD = 1000000007

n, m = [int(i) for i in input().split()]
A = [[int(i) for i in input().split()]for j in range(m)]    # nは行数

tmp = 0
res = 0

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1 for i in range(n)]

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
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

    @property
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    @property
    def group_count(self):
        return len(self.roots)

    @property
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots)

uf = UnionFind(n)
for i in range(m):
    x, y = A[i]
    uf.union(x - 1, y - 1)
for i in uf.roots:
    res = max(res, uf.size(i))

print(res)

