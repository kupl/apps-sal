# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/12 23:03

"""

n, m, k = list(map(int, input().split()))

a = []
for i in range(n):
    a.append([int(x) for x in input().split()])


removed = 0
score = 0
for c in range(m):
    count, sr = 0, 0
    for r in range(n):
        tc = sum([a[x][c] for x in range(r, min(r+k, n))])
        if tc > count:
            count = tc
            sr = r
    score += count
    removed += sum([a[r][c] for r in range(sr)])

print(score, removed)



