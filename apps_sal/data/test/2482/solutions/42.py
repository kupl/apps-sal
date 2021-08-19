from decimal import ROUND_HALF_UP, Decimal
from collections import deque, Counter, defaultdict
from bisect import bisect_left as bileft, bisect_right as biright
from functools import lru_cache
from math import sqrt, ceil
import sys
mod = 10 ** 9 + 7
inf = float('inf')


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(11451419)


class UnionFind:

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
                (xx, yy) = (yy, xx)
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
        return [i for (i, x) in enumerate(self.parents) if x < 0]

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def state_grouping(self):
        return list(self.all_group_members().values())


(n, k, l) = map(int, input().split())
uf = UnionFind(n)
uf2 = UnionFind(n)
for i in range(k):
    (p, q) = map(int, input().split())
    p -= 1
    q -= 1
    uf.union(p, q)
for i in range(l):
    (p, q) = map(int, input().split())
    p -= 1
    q -= 1
    if 1:
        uf2.union(p, q)
C = Counter([(uf.find(i), uf2.find(i)) for i in range(n)])
ANS = [0] * n
for i in range(n):
    ANS[i] = C[uf.find(i), uf2.find(i)]
print(*ANS)
