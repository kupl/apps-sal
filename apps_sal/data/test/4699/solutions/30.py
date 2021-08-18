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


n, k = readInts()
D = Counter(readInts())


def ok(n):
    while n:
        v = n % 10
        if D[v]:
            return False
        n //= 10
    return True


ans = n
for i in range(n, 100000):
    if ok(i):
        ans = i
        break
print(ans)
