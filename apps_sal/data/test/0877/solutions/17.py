# coding: utf-8





import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect

def array2d(d1, d2, init = None):
    return [[init for _ in range(d1)] for _ in range(d2)]

n, m = list(map(int, input().split(" ")))

div1 = [n]
div2 = [1]

for i in range(m):
    u, v = list(map(int, input().split(" ")))
    if u > v:
        u, v = (v, u)
    div1.append(v)
    div2.append(u)

min_div1 = min(div1)
max_div2 = max(div2)
if min_div1 < max_div2:
    print(0)
else:
    print(min_div1 - max_div2)


