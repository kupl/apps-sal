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
MAXN = 10 ** 5 + 10
MOD = 10 ** 9 + 7


def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False
    return True


def mhd(a, b):
    return abs(a[0] - b[0]) + abs(b[1] - a[1])


def charIN(x=' '):
    return sys.stdin.readline().strip().split(x)


def arrIN(x=' '):
    return list(map(int, sys.stdin.readline().strip().split(x)))


def eld(x, y):
    a = y[0] - x[0]
    b = x[1] - y[1]
    return (a * a + b * b) ** 0.5


def lgcd(a):
    g = a[0]
    for i in range(1, len(a)):
        g = math.gcd(g, a[i])
    return g


def ms(a):
    msf = -MAX
    meh = 0
    st = en = be = 0
    for i in range(len(a)):
        meh += a[i]
        if msf < meh:
            msf = meh
            st = be
            en = i
        if meh < 0:
            meh = 0
            be = i + 1
    return (msf, st, en)


def ncr(n, r):
    num = den = 1
    for i in range(r):
        num = num * (n - i) % MOD
        den = den * (i + 1) % MOD
    return num * pow(den, MOD - 2, MOD) % MOD


def flush():
    return sys.stdout.flush()


def fac(n):
    ans = 1
    for i in range(1, n + 1):
        ans *= i
        ans %= MOD
    return ans


'*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*'
n = int(input())
a = arrIN()
a.sort()
f = [1] * n
cnt = 0
for i in range(n):
    if f[i]:
        cnt += 1
        for j in range(i, n):
            if f[j] and a[j] % a[i] == 0:
                f[j] = 0
        f[i] = 0
print(cnt)
