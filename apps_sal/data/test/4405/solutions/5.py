
import math
import collections
import bisect
import heapq
import time
import itertools
import sys

"""
created by shhuan at 2018/11/16 23:49

"""
N = int(input())
A = [int(x) for x in input().split()]

wc = collections.Counter(A)

counts = [c for w, c in wc.items()]
counts.sort()
lencounts = len(counts)

vals = {v: v for v in range(1, counts[0] + 1)}
for i in range(1, lencounts):
    new_vals = {}
    for v in range(1, counts[i] + 1):
        if v % 2 == 0:
            new_vals[v] = (vals[v // 2] + v) if v // 2 in vals else v
        else:
            new_vals[v] = v

    for k, v in new_vals.items():
        if k in vals:
            vals[k] = max(vals[k], v)
        else:
            vals[k] = v

print(max(vals.values()))
