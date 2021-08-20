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
mod = 998244353
INF = float('inf')
readline = stdin.readline


def readInts():
    return list(map(int, readline().split()))


def readTuples():
    return tuple(map(int, readline().split()))


def I():
    return int(readline())


n = I()
g = 0
lcm = 1
for i in range(n):
    A = I()
    g = math.gcd(A, g)
    if i == 0:
        lcm = A
    else:
        lcm = lcm * A // g
    g = lcm
print(lcm)
