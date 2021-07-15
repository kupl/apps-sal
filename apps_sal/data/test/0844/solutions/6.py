# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/12 22:12

"""

n = int(input())
s = input()
# n = 100000
# s = ''
# for i in range(n):
#     x = random.randint(1, 10)
#     if x >= 5:
#         s += '1'
#     else:
#         s += '0'
#
# t0 = time.time()

# n = 8
# s = '11010111'

ones = [0] * (n+1)
for i in range(1, n+1):
    ones[i] = ones[i-1]
    ones[i] += s[i-1] == '1'
ones = [2*x for x in ones]
ones = [(x-i, i) for i,x in enumerate(ones)]

ds = collections.defaultdict(list)
for d, i in ones:
    ds[d].append(i)

# print(ones)
# print(ds)
ans = 0
for k, v in list(ds.items()):
    ans = max(ans, max(v)-min(v))

print(ans)
# print(time.time() - t0)



