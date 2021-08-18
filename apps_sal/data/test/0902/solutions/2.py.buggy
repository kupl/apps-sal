import math
import re
import os
import string
import sys


def ria():
    return [int(i) for i in input().split()]


def ri():
    return int(input())


def rfa():
    return [float(i) for i in input().split()]


eps = 1e-9


def is_equal(a, b):
    return abs(a - b) <= eps


def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2)


def distance_sqr(p0, p1):
    return (p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2


n, k = ria()
ar = ria()
mx = max(ar)
keka = 0
cur = ar[0]
mp = {}
for i in ar:
    mp[i] = 0
for i in ar:

    if cur == mx:
        print(mx)
        return

    if i == cur:
        continue
    if mp[cur] == k:
        print(cur)
        return
    if i > cur:
        mp[i] += 1
        cur = i
    else:
        mp[cur] += 1

    if mp[cur] == k:
        print(cur)
        return
    keka += 1

print(mx)
