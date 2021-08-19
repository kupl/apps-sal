import sys
import bisect
import math
import itertools
import string
import queue
import copy
mod = 10 ** 9 + 7


def inp():
    return int(input())


def inpm():
    return list(map(int, input().split()))


def inpl():
    return list(map(int, input().split()))


def inpls():
    return list(input().split())


def inplm(n):
    return list((int(input()) for _ in range(n)))


def inplL(n):
    return [list(input()) for _ in range(n)]


def inplT(n):
    return [tuple(input()) for _ in range(n)]


def inpll(n):
    return [list(map(int, input().split())) for _ in range(n)]


def inplls(n):
    return sorted([list(map(int, input().split())) for _ in range(n)])


(n, k) = inpm()
A = sorted(inpl())
f = [1]
for i in range(1, n + 1):
    f.append(f[-1] * i % mod)


def comb(n, r):
    if n <= 0 or r <= 0:
        return 0
    x = f[n] % mod
    y = f[r] * f[n - r] % mod
    return x * pow(y, mod - 2, mod) % mod


ans = 0
for i in range(n):
    c = comb(n - i - 1, k - 1)
    ans += A[n - 1 - i] * c - A[i] * c
    ans %= mod
    if c == 1:
        break
print(ans)
