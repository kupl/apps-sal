from sys import stdin
from math import gcd
from itertools import combinations, permutations, accumulate, product
from collections import deque, defaultdict, Counter
import decimal
import re
import math
import bisect
import heapq
import sys
sys.setrecursionlimit(10000000)
mod = 10 ** 9 + 7
INF = float('inf')
readline = stdin.readline


def readInts():
    return list(map(int, readline().split()))


def readTuples():
    return tuple(map(int, readline().split()))


def I():
    return int(readline())


class WarshallFloyd(object):

    def __init__(self):
        self.max_v = 10
        self.min_dist = [readInts() for _ in range(10)]

    def compute(self):
        for (k, i, j) in product(list(range(self.max_v)), repeat=3):
            self.min_dist[i][j] = min(self.min_dist[i][j], self.min_dist[i][k] + self.min_dist[k][j])

    def solve(self, n):
        if n == 1:
            return 0
        else:
            return self.min_dist[n][1]


(h, w) = readInts()
w = WarshallFloyd()
w.compute()
ans = 0
A = [readInts() for _ in range(h)]
for a in A:
    for i in a:
        if i == -1:
            continue
        ans += w.solve(i)
print(ans)
