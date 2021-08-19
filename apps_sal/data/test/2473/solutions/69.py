import sys
import re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, atan, degrees
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from bisect import bisect


def input():
    return sys.stdin.readline().strip()


def INT():
    return int(input())


def MAP():
    return list(map(int, input().split()))


def LIST():
    return list(map(int, input().split()))


sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7
(N, K) = MAP()
xy = [LIST() for _ in range(N)]
ans = INF
xy.sort()
for l in range(N - K + 1):
    for r in range(l + K, N + 1):
        y = sorted(xy[l:r], key=lambda x: x[1])
        for i in range(r - l - K + 1):
            sq = (xy[r - 1][0] - xy[l][0]) * (y[i + K - 1][1] - y[i][1])
            ans = min(ans, sq)
print(ans)
