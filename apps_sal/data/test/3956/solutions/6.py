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
    pairs = (i - 2) // 2
    k -= pairs
    n -= pairs
    if n < 0 or k <= 0:
        return 0
    elif k == 1 and n >= 2:
        return 0
    if n == 0:
        ans = 1
    else:
        ans = 0
        for x in range(2):
            ball = n - x
            box = k - 1
            ans += Comb(box - 1 + ball, ball) % mod
    ans *= pow(2, pairs, mod)
    return ans % mod


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
