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


s = input()
l = len(s)
ans = [1] * l
for i in range(l):
    if s[i] == 'R' and s[i + 1] == 'R':
        ans[i + 2] += ans[i]
        ans[i] = 0
for i in range(l - 1, 0, -1):
    if s[i - 1] == 'L' and s[i] == 'L':
        ans[i - 2] += ans[i]
        ans[i] = 0
print((*ans))
