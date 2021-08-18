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
s = input()
ans = ""
prv = None
for i in range(n):
    if i == 0:
        prv = s[i]
        ans += s[i]
        continue
    if s[i] == prv:
        continue
    else:
        prv = s[i]
        ans += s[i]
print((len(ans)))
