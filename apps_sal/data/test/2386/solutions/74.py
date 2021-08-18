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


N = I()
A = readInts()
S = []
for i in range(N):
    S.append(A[i] - (i + 1))
S = sorted(S)
nya = []
nya.append(S[min(N // 2 + 1, N - 1)])
nya.append(S[N // 2])
nya.append(S[N // 2 - 1])
ans = INF
for n in nya:
    wa = 0
    for i in range(N):
        wa += abs(A[i] - (n + (i + 1)))
    ans = min(ans, wa)
print(ans)
