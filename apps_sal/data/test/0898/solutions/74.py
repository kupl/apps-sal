from sys import stdin
from fractions import gcd
from itertools import combinations, permutations, accumulate, product
from collections import deque, defaultdict, Counter
import decimal
import re
import math
import bisect
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


n, m = readInts()


def yaku(m):
    ans = []
    i = 1
    while i * i <= m:
        if m % i == 0:
            j = m // i
            ans.append(i)
            if j != i:
                ans.append(j)
        i += 1
    ans = sorted(ans)
    return ans


dic = yaku(m)
ans = 1
for k in dic:
    if k * n <= m:
        ans = max(ans, k)
print(ans)
