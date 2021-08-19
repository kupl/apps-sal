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
for _ in range(int(input())):
    n = int(input())
    s = [i for i in input()]
    t = [i for i in input()]
    d = defaultdict(int)
    for i in range(n):
        d[s[i]] += 1
        d[t[i]] += 1
    if len(list(d.keys())) > n or sum((i % 2 for i in list(d.values()))):
        print('No')
    else:
        ans = []
        for i in range(n):
            if s[i] != t[i]:
                for j in range(i + 1, n):
                    if s[j] != t[j]:
                        if s[i] == s[j]:
                            ans.append([j, i])
                            (s[j], t[i]) = (t[i], s[j])
                            break
                        elif s[i] == t[j]:
                            ans.append([j, j])
                            (s[j], t[j]) = (t[j], s[j])
                            ans.append([j, i])
                            (s[j], t[i]) = (t[i], s[j])
                            break
                        elif t[i] == t[j]:
                            ans.append([i, j])
                            (s[i], t[j]) = (t[j], s[i])
                            break
                        elif t[i] == s[j]:
                            ans.append([j, j])
                            (s[j], t[j]) = (t[j], s[j])
                            ans.append([i, j])
                            (s[i], t[j]) = (t[j], s[i])
                            break
        print('Yes')
        print(len(ans))
        for i in ans:
            print(i[0] + 1, i[1] + 1)
