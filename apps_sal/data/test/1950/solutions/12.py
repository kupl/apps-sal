# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2017/11/8 09:35

"""


N = int(input())
A = [int(x) for x in input().split()]


if N % 2 == 0:
    A.append(0)

heapq.heapify(A)
ans = 0
while len(A) > 1:
    i = 0
    p = 0
    while A and i < 3:
        p += heapq.heappop(A)
        i += 1
    heapq.heappush(A, p)
    ans += p
print(ans)
