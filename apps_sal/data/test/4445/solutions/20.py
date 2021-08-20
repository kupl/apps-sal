import sys
import math
import heapq
import bisect
from collections import defaultdict as dd
n = int(input())
l = [int(i) for i in input().split()]
o = []
e = []
for i in l:
    if i % 2 == 0:
        e.append(i)
    else:
        o.append(i)
o.sort()
e.sort()
if len(e) > len(o):
    (o, e) = (e, o)
for i in range(len(e)):
    e.pop(-1)
    o.pop(-1)
if o:
    o.pop(-1)
print(sum(o))
