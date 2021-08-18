from sys import stdin
from fractions import gcd
from itertools import combinations, permutations, accumulate, product
from collections import deque, defaultdict, Counter
import decimal
import re
import math
import bisect
import heapq
import sys
sys.setrecursionlimit(10000000)
mod = 10**9 + 7
readline = stdin.readline


def readInts():
    return list(map(int, readline().split()))


def readTuples():
    return tuple(map(int, readline().split()))


def I():
    return int(readline())


n = I()
L = readInts()
L = sorted(L)
ans = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        a = L[i]
        b = L[j]
        c = bisect.bisect_left(L, a + b)
        ans += c - (j + 1)
print(ans)
