from sys import stdin
from fractions import gcd
from itertools import combinations, permutations, accumulate, product
from collections import deque, defaultdict, Counter
import decimal
import re
import math
import sys
sys.setrecursionlimit(10000000)
mod = 10 ** 9 + 7
readline = stdin.readline


def readInts():
    return list(map(int, readline().split()))


def readTuples():
    return tuple(map(int, readline().split()))


def I():
    return int(readline())


x = I()
ans = 0
if x >= 11:
    el = x // 11
    ans += el * 2
    x -= 11 * el
if 0 < x <= 6:
    ans += 1
elif 6 < x < 11:
    ans += 2
print(ans)
