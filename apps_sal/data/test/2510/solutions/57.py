import collections
import fractions
import itertools
import functools
import bisect
import heapq
import math
import operator
import sys
sys.setrecursionlimit(10 ** 9 + 7)
(N, M) = list(map(int, input().split()))


class UnionFind:

    def __init__(self, n):
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

    def size(self, n):
        return -self.parents[self.find(n)]


def solve():
    group = UnionFind(N)
    for i in range(M):
        (a, b) = [int(x) - 1 for x in input().split()]
        group.union(a, b)
    ans = 0
    for i in range(N):
        ans = max(ans, group.size(i))
    print(ans)
    return 0


def __starting_point():
    solve()


__starting_point()
