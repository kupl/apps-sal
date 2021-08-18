
import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/6 22:19

"""

t0 = time.time()
a, b, c = list(map(int, input().split()))


def ct(a, b):
    if a > b:
        a, b = b, a
    L = 998244353
    s = 1
    sx = 1
    for k in range(1, a + 1):
        s = s * (a + 1 - k) * (b + 1 - k) // k
        sx += s % L
    return sx


L = 998244353

print(ct(a, b) * ct(a, c) * ct(b, c) % L)
