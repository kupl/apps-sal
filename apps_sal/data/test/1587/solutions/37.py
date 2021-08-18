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
INF = float('inf')
readline = stdin.readline


def readInts():
    return list(map(int, readline().split()))


def readTuples():
    return tuple(map(int, readline().split()))


def I():
    return int(readline())


n = I()
s = input()
C = Counter(s)
w, r = 0, 0
for k, v in list(C.items()):
    if k == 'W':
        w += v
    else:
        r += v
p = 'R' * r + 'W' * w
ans = 0
for i in range(n):
    if p[i] == s[i]:
        pass
    else:
        ans += 1
print((ans // 2))
