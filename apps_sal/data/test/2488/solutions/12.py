#!/usr/bin python3
# -*- coding: utf-8 -*-

from bisect import bisect_left, bisect_right

n, d, a = list(map(int, input().split()))
x = []
xh = dict()
for _ in range(n):
    xi, hi = list(map(int, input().split()))
    x.append(xi)
    xh[xi] = hi
x.sort()

l = 0
ret = 0
ai = [0] * (n + 1)
anow = 0
while l < n:
    xl = x[l]
    hl = xh[xl]
    anow += ai[l]
    hl -= a * anow
    if hl > 0:
        r = bisect_right(x, xl + 2 * d)
        k = (hl + (a - 1)) // a
        ret += k
        anow += k
        ai[r] -= k
    l += 1
print(ret)
