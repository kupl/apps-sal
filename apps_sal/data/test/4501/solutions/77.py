import sys
import re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees, log2, gcd
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from heapq import heappush, heappop
from functools import reduce, lru_cache
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return list(map(int, input().split()))
def LIST(): return list(map(int, input().split()))
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return list(zip(*(MAP() for _ in range(n))))


sys.setrecursionlimit(10 ** 9)
INF = 10**6
mod = 10 ** 9 + 7

N, A = MAP()
x = LIST()

big = []
small = []
cnt = 0

for y in x:
    if y == A:
        cnt += 1
    elif y < A:
        small.append(A - y)
    else:
        big.append(y - A)

big_possible = [0] * 2501
small_possible = [0] * 2501
big_possible[0] = 1
small_possible[0] = 1

for a in big:
    for i in range(2500 - a, -1, -1):
        if big_possible[i]:
            big_possible[i + a] += big_possible[i]

for b in small:
    for i in range(2500 - b, -1, -1):
        if small_possible[i]:
            small_possible[i + b] += small_possible[i]

ans = 1
for i in range(1, 2501):
    ans += small_possible[i] * big_possible[i]


ans *= 2**cnt
print((ans - 1))
