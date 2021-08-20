from bisect import *
from collections import *
from itertools import *
import functools
import sys
import math
from decimal import *
from copy import *
from heapq import *
getcontext().prec = 30
MAX = sys.maxsize
MAXN = 1000010
MOD = 10 ** 9 + 7
spf = [i for i in range(MAXN)]


def sieve():
    for i in range(2, MAXN, 2):
        spf[i] = 2
    for i in range(3, int(MAXN ** 0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, MAXN, i):
                if spf[j] == j:
                    spf[j] = i


def fib(n, m):
    if n == 0:
        return [0, 1]
    else:
        (a, b) = fib(n // 2)
        c = a % m * (b % m * 2 - a % m) % m
        d = a % m * (a % m) % m + b % m * b % m % m
        if n % 2 == 0:
            return [c, d]
        else:
            return [d, c + d]


def charIN(x=' '):
    return sys.stdin.readline().strip().split(x)


def arrIN(x=' '):
    return list(map(int, sys.stdin.readline().strip().split(x)))


def ncr(n, r):
    num = den = 1
    for i in range(r):
        num = num * (n - i) % MOD
        den = den * (i + 1) % MOD
    return num * pow(den, MOD - 2, MOD) % MOD


def flush():
    return sys.stdout.flush()


'*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*'
(n, k) = arrIN()
a = arrIN()
st = []
ls = 0
f = defaultdict(int)
j = 0
for i in a:
    if f[i] == 0:
        if ls < k:
            st.append(i)
            f[i] = 1
            ls += 1
        else:
            f[st[j]] = 0
            j += 1
            st.append(i)
            f[i] = 1
print(len(st) - j)
for i in range(len(st) - 1, j - 1, -1):
    print(st[i], end=' ')
