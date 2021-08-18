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


n = I()
X = readInts()
nya = sorted(X)
m1 = nya[n // 2 - 1]
m2 = nya[n // 2]
for x in X:
    if x <= m1:
        print(m2)
    else:
        print(m1)
