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


class UnionFind:

    def __init__(self, N):
        self.table = [i for i in range(N)]
        self.rank = [1 for i in range(N)]
        self.size = [1 for i in range(N)]

    def Find(self, x):
        if self.table[x] == x:
            return x
        else:
            self.table[x] = self.Find(self.table[x])
            self.size[x] = self.size[self.table[x]]
            return self.table[x]

    def Unite(self, x, y):
        (x, y) = (self.Find(x), self.Find(y))
        (sx, sy) = (self.Size(x), self.Size(y))
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            self.table[y] = x
            self.size[x] = sx + sy
        else:
            self.table[x] = y
            self.size[y] = sx + sy
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def Check(self, x, y):
        return self.Find(x) == self.Find(y)

    def Size(self, x):
        return self.size[self.Find(x)]


N = int(input())
UF = UnionFind(10 ** 5 + 1)
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
        if not UF.Check(s, t):
            UF.Unite(s, t)
ans = 0
for x in xx:
    s = tatedict[x][0]
    ans += UF.Size(s) - len(tatedict[x])
print(ans)
