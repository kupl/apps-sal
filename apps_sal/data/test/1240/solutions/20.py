import math
import sys
import re
import itertools
import pprint
import collections
ri, rai = lambda: int(input()), lambda: list(map(int, input().split()))

n = ri()
a = [rai() for i in range(n)]

s = 0
for l, r in a:
    s += l - r

res = 0
sres = abs(s)

for i in range(n):
    l, r = a[i]
    s -= l - r
    s += r - l
    if abs(s) > sres:
        res = i + 1
        sres = abs(s)
    s -= r - l
    s += l - r

print(res)
