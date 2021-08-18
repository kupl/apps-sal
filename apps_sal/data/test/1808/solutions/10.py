
import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/12 22:08

"""


n, k, x = map(int, input().split())

ts = [int(x) for x in input().split()]

for i in range(n - 1, n - k - 1, -1):
    ts[i] = min(ts[i], x)

print(sum(ts))
