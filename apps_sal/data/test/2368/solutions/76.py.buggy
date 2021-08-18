# -*- coding: utf-8 -*-
import math
import collections
import bisect
import itertools
import heapq
import os
from collections import defaultdict, deque, Counter
from sys import stdin
readline = stdin.readline
"""
# sys.setrecursionlimit(10 ** 9)

N = int(readline())
N, K = map(int, readline().split())
A = list(map(int, readline().split()))
L = [list(map(int, readline().split())) for _ in [0]*N]
S = readline().rstrip(os.linesep)

for _ in [0]*N:
  x, y, z = map(int, readline().split())
"""
N, M = list(map(int, readline().split()))
a = list(map(int, readline().split()))
b = list(map(int, readline().split()))


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
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in list(self.all_group_members().items()))


uf = UnionFind(N)
for _ in [0] * M:
    c, d = list(map(int, readline().split()))
    uf.union(c - 1, d - 1)

for grp in list(uf.all_group_members().values()):
    a_values = [a[x] for x in grp]
    b_values = [b[x] for x in grp]
    a_total = sum(a_values)
    b_total = sum(b_values)
    if a_total != b_total:
        print("No")
        return

print("Yes")
