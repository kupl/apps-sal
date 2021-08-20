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
mod = 10 ** 9 + 7
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


(N, S) = input().split()
N = int(N)
ans = 0
for i in range(N):
    a = 0
    t = 0
    c = 0
    g = 0
    for j in range(i, N):
        if S[j] == 'A':
            a += 1
        elif S[j] == 'T':
            t += 1
        elif S[j] == 'C':
            c += 1
        else:
            g += 1
        if a == t and c == g:
            ans += 1
print(ans)
