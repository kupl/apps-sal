import sys, re
from itertools import product
from collections import Counter
ls = [l.rstrip() for l in sys.stdin.readlines()]

n, k = list(map(int, ls[0].split(" ")))
pss = ls[1:1+n]
corr = ls[1+n]
a = list([len(x) for x in pss])
m = len(corr)
r1 = 0
for i in range(1, m):
    r1 += a.count(i)
r2 = r1 + a.count(m) - 1
# print(r1, r2)
print(r1//k*5 + r1 + 1, r2//k*5 + r2 + 1)

