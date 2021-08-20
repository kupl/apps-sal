import sys
import math
import itertools as it
import operator as op
import fractions as fr
(n, k) = map(int, sys.stdin.readline().split())
ids = list(map(int, sys.stdin.readline().split()))
p = 1
while k >= p + 1:
    k -= p
    p += 1
print(ids[k - 1])
