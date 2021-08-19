import numpy as np
import sys
import heapq as hq
import itertools
import math
import collections
def ma(): return map(int, input().split())
def lma(): return list(map(int, input().split()))
def tma(): return tuple(map(int, input().split()))
def ni(): return int(input())
def yn(fl): return print("Yes") if fl else print("No")


mod = 10**9 + 7


def ncr_1(n, r, p):  # 　n>>r の場合のncr　O(r)
    x = 1
    y = 1
    for i in range(r):
        x *= (n - i)
        y *= (i + 1)
        x %= p
        y %= p
    return x * modinv(y, p) % p


def modinv(a, p):
    b, u, v = p, 1, 0
    while b:
        t = a // b
        a -= t * b
        a, b = b, a
        u -= t * v
        u, v = v, u
    u %= p
    return u


n, m, k = ma()
ans = 0
for i in range(1, n):
    ans += i * (n - i) * m**2
    ans %= mod
for i in range(1, m):
    ans += i * (m - i) * n**2
    ans %= mod
print((ans * ncr_1(n * m - 2, k - 2, mod)) % mod)
