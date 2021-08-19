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


(n, m) = readInts()
N = [readInts() for _ in range(n)]
M = [readInts() for _ in range(m)]
for (a, b) in N:
    pos = INF
    ans = None
    for (i, (x, y)) in enumerate(M):
        if abs(a - x) + abs(b - y) < pos:
            pos = abs(a - x) + abs(b - y)
            ans = i + 1
    print(ans)
