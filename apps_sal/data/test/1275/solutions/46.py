from sys import stdin
from math import gcd
from itertools import combinations, permutations, accumulate, product, combinations_with_replacement
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
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
readline = stdin.readline


def readInts():
    return list(map(int, readline().split()))


def readTuples():
    return tuple(map(int, readline().split()))


def I():
    return int(readline())


def f(n):
    return int(math.ceil(n - 0.5))


sys.setrecursionlimit(10000000)
mod = 10**9 + 7
INF = float('inf')
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
readline = stdin.readline


def readInts():
    return list(map(int, readline().split()))


def readTuples():
    return tuple(map(int, readline().split()))


def I():
    return int(readline())


def f(n):
    return int(math.ceil(n - 0.5))


N, K = readInts()


def calc(n):
    if n <= 0 or n > 2 * N:
        return 0
    else:
        return min(n - 1, 2 * N - n + 1)


ans = 0
for AB in range(2 * N + 1):
    ans += calc(AB) * calc(AB - K)
print(ans)
