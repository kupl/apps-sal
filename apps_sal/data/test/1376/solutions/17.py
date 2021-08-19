import math
import os
import random
import re
import sys
n = int(input())
l = list(map(int, input().split()))
d = {}
for i in range(2 * n):
    if d.get(l[i], 0) == 0:
        t = []
        t.append(i)
        d[l[i]] = t
    else:
        d[l[i]].append(i)
(a, b) = (0, 0)
(c, e) = (0, 0)
k = 0
for i in sorted(d.keys()):
    z = sorted(d[i])
    if k == 0:
        a = abs(a - z[0])
        b = abs(b - z[1])
    else:
        a += abs(c - z[0])
        b += abs(e - z[1])
    c = z[0]
    e = z[1]
    k += 1
print(a + b)
