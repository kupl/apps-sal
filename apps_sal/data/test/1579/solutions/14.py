from collections import defaultdict, deque
import sys
import heapq
import bisect
import math
import itertools
import string
import queue
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
mod = 10 ** 9 + 7
eps = 10 ** (-7)


def inpl():
    return list(map(int, input().split()))


def inpl_str():
    return list(input().split())


class PotentialUnionFind:

    def __init__(self, N):
        self.table = [i for i in range(N)]
        self.rank = [1 for i in range(N)]
        self.size = [1 for i in range(N)]
        self.diffweight = [0 for i in range(N)]

    def Find(self, x):
        if self.table[x] == x:
            return x
        else:
            root = self.Find(self.table[x])
            self.size[x] = self.size[self.table[x]]
            self.diffweight[x] += self.diffweight[self.table[x]]
            self.table[x] = root
            return root

    def Unite(self, x, y, w):
        w = w - self.Weight(y) + self.Weight(x)
        (x, y) = (self.Find(x), self.Find(y))
        (sx, sy) = (self.Size(x), self.Size(y))
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            self.table[y] = x
            self.size[x] = sx + sy
            self.diffweight[y] = w
        else:
            self.table[x] = y
            self.size[y] = sx + sy
            self.diffweight[x] = -w
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def Check(self, x, y):
        return self.Find(x) == self.Find(y)

    def Size(self, x):
        return self.size[self.Find(x)]

    def Weight(self, x):
        self.Find(x)
        return self.diffweight[x]

    def Diff(self, x, y):
        return self.Weight(y) - self.Weight(x)


N = int(input())
PUF = PotentialUnionFind(10 ** 5 + 1)
xys = [inpl() for _ in range(N)]
xys.sort()
tatedict = defaultdict(list)
xx = set()
for (x, y) in xys:
    tatedict[x].append(y)
    xx.add(x)
for x in xx:
    s = tatedict[x][0]
    for t in tatedict[x]:
        if not PUF.Check(s, t):
            PUF.Unite(s, t, 1)
ans = 0
for x in xx:
    s = tatedict[x][0]
    ans += PUF.Size(s) - len(tatedict[x])
print(ans)
