import sys
import math
import itertools as it
import operator as op
import fractions as fr
(n, m, k) = map(int, sys.stdin.readline().split())
P = list(map(int, sys.stdin.readline().split()))
P = P[::-1]
r = 0
for _ in range(n):
    Aj = map(int, sys.stdin.readline().split())
    for a in Aj:
        idx = P.index(a)
        r += k - idx
        del P[idx]
        P.append(a)
print(r)
