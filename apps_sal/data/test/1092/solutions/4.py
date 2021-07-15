#!/usr/bin/env python3


mod = 10 ** 9 + 7


def factorial(n):
    x = 1
    for i in range(n):
        yield x
        x = x * (i + 1) % mod

f = list(factorial(1001))


def C(n, k):
    return f[n] * pow(f[k], mod - 2, mod) * pow(f[n - k], mod - 2, mod) % mod


n, m = [int(x) for x in input().split()]
b = [-1] + [int(x) - 1 for x in input().split()] + [n]
b.sort()

ans = 1
cur = n - m
for i in range(1, len(b)):
    l = b[i] - b[i - 1] - 1
    ans = ans * C(cur, l) % mod
    if (l > 0) and (i > 1) and (i < len(b) - 1):
        ans = ans * pow(2, l - 1, mod) % mod
    cur -= l

print(ans)

