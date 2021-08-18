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
INF = 10**6  # float('inf')
mod = 10 ** 9 + 7
#mod = 998244353
#from decimal import *
#import numpy as np
#decimal.getcontext().prec = 10


#階乗#
lim = 2 * 10**5  # 必要そうな階乗の限界を入力
fact = [1] * (lim + 1)
for n in range(1, lim + 1):
    fact[n] = n * fact[n - 1] % mod

#階乗の逆元#
fact_inv = [1] * (lim + 1)
fact_inv[lim] = pow(fact[lim], mod - 2, mod)
for n in range(lim, 0, -1):
    fact_inv[n - 1] = n * fact_inv[n] % mod


def C(n, r):
    return (fact[n] * fact_inv[r] % mod) * fact_inv[n - r] % mod


# 素因数分解
def factorization(n):
    arr = []
    tmp = n
    for i in range(2, int(-(-n**0.5 // 1)) + 1):
        if tmp % i == 0:
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i
            arr.append([i, cnt])
    if tmp != 1:
        arr.append([tmp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr


N, M = MAP()
if M == 1:
    print((1))
    return

arr = factorization(M)
ans = 1
for g, n in arr:
    ans *= C(N - 1 + n, n)
    ans %= mod

print(ans)
