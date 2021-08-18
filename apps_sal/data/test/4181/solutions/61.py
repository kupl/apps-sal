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
A = readInts()
B = readInts()
ans = 0
for i in range(n):
    v = B[i]
    nya = min(v, A[i])
    A[i] -= nya
    v -= nya
    ans += nya
    nya = min(A[i + 1], v)
    ans += nya
    A[i + 1] -= nya
print(ans)
