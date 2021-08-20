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
mod = 10 ** 9 + 7
readline = stdin.readline


def readInts():
    return list(map(int, readline().split()))


def readTuples():
    return tuple(map(int, readline().split()))


def I():
    return int(readline())


(n, m) = readInts()
A = sorted(readInts())
if n >= m:
    print(0)
else:
    dist = []
    all = 0
    for i in range(m - 1):
        dist.append(A[i + 1] - A[i])
        all += A[i + 1] - A[i]
    dist = sorted(dist, reverse=True)
    print(all - sum(dist[:n - 1]))
