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


def fun(a, n, m):
    x = [0] * n
    ans = 0
    mp = dict()
    x[0] = a[0]
    for i in range(1, n):
        x[i] = x[i - 1] ^ a[i]
    for i in range(n):
        tmp = m ^ x[i]
        if tmp in list(mp.keys()):
            ans += mp[tmp]
        if x[i] == m:
            ans += 1
        mp[x[i]] = mp.get(x[i], 0) + 1
    return ans


n = int(input())
a = arrIN()
x = []
for i in a:
    if i > 0:
        x.append(1)
    else:
        x.append(-1)
ans = fun(x, n, -1) + fun(x, n, -2)
print(ans, n * (n + 1) // 2 - ans)
