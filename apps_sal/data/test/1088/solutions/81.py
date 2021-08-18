from decimal import ROUND_HALF_UP, Decimal
from fractions import Fraction as frac
from itertools import combinations as com, permutations as per
from bisect import bisect_left as bileft, bisect_right as biright, insort
from functools import lru_cache
import sys
try:
    import os
    f = open('input.txt', 'r')
    sys.stdin = f
except FileNotFoundError:
    None
from math import sqrt, ceil, floor
from collections import deque, Counter, defaultdict
def input(): return sys.stdin.readline().strip()


sys.setrecursionlimit(11451419)

n, k = list(map(int, input().split()))
A = [list(map(int, input().split())) for i in range(n)]
cntx = 0
cnty = 0

kai = [1] * 70
mod = 998244353
for i in range(1, 65):
    kai[i] = (kai[i - 1] * i) % mod


class UnionFind():
    def __init__(self, num):
        self.n = num
        self.parents = [-1 for i in range(self.n)]

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])

            return self.parents[x]

    def union(self, x, y):
        xx = self.find(x)
        yy = self.find(y)
        if xx == yy:
            return
        else:
            size_xx = abs(self.parents[xx])
            size_yy = abs(self.parents[yy])
            if size_xx > size_yy:
                xx, yy = yy, xx

            self.parents[yy] += self.parents[xx]
            self.parents[xx] = yy

    def size(self, x):
        xx = self.find(x)
        return abs(self.parents[xx])

    def same(self, x, y):
        return 1 if self.find(x) == self.find(y) else 0

    def members(self, x):
        xx = self.find(x)
        return [i for i in range(self.n) if self.find(i) == xx]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def state_grouping(self):
        return list(self.all_group_members().values())


ufx = UnionFind(n)
ufy = UnionFind(n)

for i in range(n):
    po = 0
    for j in range(i):
        for p in range(n):
            if A[i][p] + A[j][p] > k:
                po = 1
                break
        else:
            ufx.union(i, j)

for i in range(n):
    for j in range(n):
        for p in range(n):
            if A[p][i] + A[p][j] > k:
                break
        else:
            ufy.union(i, j)

xx = 1
yy = 1
for i in ufx.parents:
    if i < -1:
        xx *= kai[abs(i)]
        xx %= mod
for j in ufy.parents:
    if j < -1:
        yy *= kai[abs(j)]
        yy %= mod

print((xx * yy % mod))
