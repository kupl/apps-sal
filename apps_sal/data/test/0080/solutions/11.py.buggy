#!/usr/bin/env python3

from math import sqrt

[l, r, x, y] = list(map(int, input().strip().split()))

if y % x != 0:
    print(0)
    return

y = y // x
l = -((-l) // x)  # ceil
r = r // x

pr = []
i = 2
yx = y
mx = sqrt(yx)
while i <= mx:
    d = 1
    while yx % i == 0:
        d *= i
        yx //= i
    if d > 1:
        pr.append(d)
        mx = sqrt(yx)
    i += 1

if yx > 1:
    pr.append(yx)


def count(a, ar):
    if len(ar) == 0:
        if l <= a <= r and l <= y // a <= r:
            return 1
        else:
            return 0
    res = 0
    res += count(a, ar[1:])
    aa = a * ar[0]
    if aa <= r and y // aa >= l:
        res += count(aa, ar[1:])
    return res


res = count(1, pr)
print(res)
