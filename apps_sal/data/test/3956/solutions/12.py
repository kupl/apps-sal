from collections import defaultdict, deque
import sys
import heapq
import bisect
import math
import itertools
import string
import queue
import datetime
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
mod = 998244353
eps = 10 ** (-7)


def inp():
    return int(input())


def inpl():
    return list(map(int, input().split()))


def inpls():
    return list(input().split())


(K, N) = inpl()
MAX = K + N + 10
fac = [1] * (MAX + 1)
for i in range(1, MAX + 1):
    fac[i] = fac[i - 1] * i % mod
gyakugen = [1] * (MAX + 1)
gyakugen[MAX] = pow(fac[MAX], mod - 2, mod)
for i in range(MAX, 0, -1):
    gyakugen[i - 1] = gyakugen[i] * i % mod


def Comb(n, k):
    return fac[n] * gyakugen[k] * gyakugen[n - k] % mod


def calc(k, n, i):
    x = (i - 2) // 2
    k -= x
    n -= x
    if k == 1:
        if n <= 1:
            return n
        else:
            return 0
    elif n == 0:
        return pow(2, x, mod)
    elif n < 0 or k <= 0:
        return 0
    tmp = 0
    for j in range(2):
        zb = n - j
        zm = k - 2
        tmp += Comb(zb + zm, zb) % mod
    tmp %= mod
    tmp *= pow(2, x, mod)
    return tmp


ans = []
for i in range(2, K + 2):
    if i % 2 == 0:
        pairs = (i - 2) // 2
        tmp = 0
        for p0 in range(pairs + 1):
            tmp += calc(K - p0 * 2, N, i - p0 * 2) * Comb(pairs, p0) % mod
            tmp %= mod
    ans.append(tmp)
    print(tmp)
ans = ans[::-1]
for i in range(1, K):
    print(ans[i])
