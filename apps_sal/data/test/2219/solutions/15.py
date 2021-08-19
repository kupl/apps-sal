from bisect import *
from collections import *
from itertools import *
import functools
import sys
from math import *
from decimal import *
from copy import *
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


def dis(x, y):
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


def flush():
    return sys.stdout.flush()


'*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*'
for _ in range(int(input())):
    (n, k) = arrIN()
    ans = 0
    while 1:
        if n % k == 0:
            n //= k
            ans += 1
        else:
            x = n % k
            ans += x
            n -= x
        if n == 0:
            print(ans)
            break
