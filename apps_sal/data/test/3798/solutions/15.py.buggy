# -*- coding: utf-8 -*-
from math import sqrt
n = int(input())
s = int(input())


def f(b, n):
    ans = 0
    while n >= b:
        ans += n % b
        n = n // b
    return ans + n


if n == s:
    print(n + 1)
    return

for b in range(2, int(sqrt(n)) + 1):
    if f(b, n) == s:
        print(b)
        break
else:
    for p in range(1, int(sqrt(n)) + 1)[::-1]:
        d, m = divmod(p + n - s, p)
        if m == 0 and d >= 2 and f(d, n) == s:
            print(d)
            break
    else:
        print(-1)
