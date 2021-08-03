import sys
import math
import itertools as it
import operator as op
import fractions as fr

# n,m = map(int,sys.stdin.readline().split())
n = int(sys.stdin.readline().strip())
T = list(map(int, sys.stdin.readline().split()))

d = 0
for t in T:
    if t - d > 15:
        break
    else:
        d = t

d = min(d + 15, 90)
print(d)
