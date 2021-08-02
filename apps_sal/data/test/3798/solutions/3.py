#!/usr/bin/env python3
import math


def f(b, n):
    return n if (n < b) else f(b, n // b) + n % b


n = int(input())
s = int(input())

ans = -1
if n == s:
    ans = n + 1
else:
    for b in range(2, math.floor(n ** 0.5) + 1):
        if f(b, n) == s:
            ans = b
            break
    else:
        for p in range(1, math.ceil(n ** 0.5)):
            if (n - s) % p != 0:
                continue
            b = (n - s) // p + 1
            if math.floor(n ** 0.5) < b <= n and f(b, n) == s:
                ans = b
print(ans)
