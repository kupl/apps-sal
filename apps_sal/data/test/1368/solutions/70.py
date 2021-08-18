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
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))


sys.setrecursionlimit(10 ** 9)
INF = 10**6
mod = 998244353

lim = 50
fact = [1] * (lim + 1)
for n in range(1, lim + 1):
    fact[n] = n * fact[n - 1]


def C(n, r):
    return fact[n] // fact[n - r] // fact[r]


N, A, B = MAP()
v = sorted(LIST(), reverse=True)

V_cnt = Counter(v)
V_max = Counter(v[:A])
key = v[A - 1]
print(sum(v[:A]) / A)

v = v[::-1]

idx_1 = bisect_left(v, key)
idx_2 = bisect(v, key)
n = idx_2 - idx_1
k = bisect(v, key)
m = N - k


if m == 0:
    ans = 0
    for i in range(A, min(B - m, n) + 1):
        ans += C(n, i)
    print(ans)
else:
    print(C(n, A - m))
