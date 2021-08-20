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


n = I()
A = readInts()
is_ok = [0] * (10 ** 6 + 1)
se = set(A)
C = Counter(A)
for a in se:
    for b in range(a, 10 ** 6 + 1, a):
        is_ok[b] += 1
ans = 0
for i in range(n):
    if C[A[i]] >= 2:
        continue
    if is_ok[A[i]] == 1:
        ans += 1
print(ans)
