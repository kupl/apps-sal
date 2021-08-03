import sys
import math
import itertools as it
import operator as op
import fractions as fr

n, m = map(int, sys.stdin.readline().split())


l, r = 1, n - 1
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if a > b:
        a, b = b, a
    l = max(l, a)
    r = min(r, b - 1)

if l <= r:
    r = r - l + 1
else:
    r = 0

print(r)
