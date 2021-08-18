from sys import stdin
from fractions import gcd
from itertools import combinations, permutations, accumulate, product
from collections import deque, defaultdict, Counter
import decimal
import re
import math

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
ans = 0
for bit in range(1 << len(s) - 1):
    st = s[0]
    wa = 0
    for i in range(len(s) - 1):
        if bit & (1 << i):
            wa += int(st)
            st = s[i + 1]
        else:
            st += s[i + 1]
    ans += wa + int(st)
print(ans)
