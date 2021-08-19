#!/usr/bin/env python3
import sys


def rint():
    return list(map(int, sys.stdin.readline().split()))
#lines = stdin.readlines()


n, m = rint()

a = list(map(int, input()))
b = list(map(int, input()))
a = a[::-1]
b = b[::-1]
div = 998244353

mod_bit = [0] * (2 * 10**5 + 1)
mod_asum = [0] * (2 * 10**5 + 1)

mod_bit[0] = 1 % div
for i in range(1, n):
    mod_bit[i] = mod_bit[i - 1] * 2 % div
mod_asum[0] = a[0]
for i in range(1, n):
    mod_asum[i] = (mod_asum[i - 1] + a[i] * mod_bit[i]) % div

ans = 0
for i in range(m):
    ans += b[i] * mod_asum[min(i, n - 1)]
    ans %= div

print(ans)
