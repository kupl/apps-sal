#!/usr/bin/env python3

import sys

n = int(sys.stdin.readline().strip())
xis = list(map(int, sys.stdin.readline().strip().split()))


xmin = min(xis)
xmax = max(xis)
if xmax - xmin != 2:
    print(n)
    print(' '.join(map(str, xis)))
    return

xm = (xmin + xmax) // 2

a = xis.count(xmin)
b = xis.count(xm)
c = xis.count(xmax)

edg = min(a, c)
mid = b // 2
if edg > mid:
    k = -edg
else:
    k = mid
target = a + b + c - 2 * abs(k)
A = a + k
B = b - 2 * k
C = c + k
yis = ([xmin] * A) + ([xm] * B) + ([xmax] * C)

print(target)
print(' '.join(map(str, yis)))
