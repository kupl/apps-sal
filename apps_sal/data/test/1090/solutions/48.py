from fractions import gcd
from itertools import combinations, permutations, accumulate
from collections import deque, defaultdict, Counter
import decimal
import re

import sys
sys.setrecursionlimit(10000000)
mod = 10**9 + 7


def readInts():
    return list(map(int, input().split()))


def I():
    return int(input())


n, k = readInts()
S = input()
a = 0
for i in range(1, len(S)):
    if S[i] != S[i - 1]:
        a += 1
print((n - 1 - max(a - 2 * k, 0)))
