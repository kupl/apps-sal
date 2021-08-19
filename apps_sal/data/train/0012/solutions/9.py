from bisect import *
from collections import *
from itertools import *
import functools
import sys
import math
from decimal import *
from copy import *
from heapq import *
from fractions import *
getcontext().prec = 30
MAX = sys.maxsize
MAXN = 300010
MOD = 10 ** 9 + 7
spf = [i for i in range(MAXN)]
spf[0] = spf[1] = -1


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


def solve():
    n = int(input())
    a = arrIN()
    b = arrIN()
    x = [[0, 0, 0] for i in range(n)]
    for i in range(n):
        x[i][0] = int(a[i] == -1)
        x[i][1] = int(a[i] == 0)
        x[i][2] = int(a[i] == 1)
        x[i][0] |= x[i - 1][0]
        x[i][1] |= x[i - 1][1]
        x[i][2] |= x[i - 1][2]
    if a[0] != b[0]:
        print('NO')
    else:
        for i in range(1, n):
            if a[i] != b[i]:
                if a[i] > b[i]:
                    if not x[i - 1][0]:
                        print('NO')
                        break
                elif not x[i - 1][2]:
                    print('NO')
                    break
        else:
            print('YES')


t = int(input())
for i in range(t):
    solve()
