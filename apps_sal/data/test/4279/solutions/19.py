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
MAXN = 10**6 + 1
MOD = 10**9 + 7
spf = [i for i in range(MAXN)]


def sieve():
    for i in range(2, MAXN, 2):
        spf[i] = 2
    for i in range(3, int(MAXN**0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, MAXN, i):
                if spf[j] == j:
                    spf[j] = i


def mhd(a, b):
    return abs(a[0] - b[0]) + abs(b[1] - a[1])


def charIN(x=' '):
    return(sys.stdin.readline().strip().split(x))


def arrIN(x=' '):
    return list(map(int, sys.stdin.readline().strip().split(x)))


def eld(x, y):
    a = y[0] - x[0]
    b = x[1] - y[1]
    return (a * a + b * b)**0.5


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
    return msf, st, en


def ncr(n, r):
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % MOD
        den = (den * (i + 1)) % MOD

    return (num * (pow(den, MOD - 2, MOD))) % MOD


def flush():
    return sys.stdout.flush()


'''*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*'''
cnt = 0
pre = [0] * MAXN
temp = [0] * MAXN
for i in range(1, MAXN):
    cnt += len(str(i))
    temp[i] = cnt
    pre[i] = cnt + pre[i - 1]

for _ in range(int(input())):
    k = int(input())
    idx = bisect_left(pre, k)
    if pre[idx] == k:
        print(str(idx)[-1])
    else:
        rem = k - pre[idx - 1]
        x = bisect_left(temp, rem)
        if temp[x] == rem:
            print(str(x)[-1])
        else:
            rem1 = rem - temp[x - 1]
            s = str(x)
            c = 0
            for i in s:
                c += 1
                if c == rem1:
                    print(i)
                    break
