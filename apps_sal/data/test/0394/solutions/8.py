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
created by shhuan at 2018/10/20 22:37

"""

"""
# Definition for a Node.
"""



N = int(input())
A = [0] + [int(x) for x in input().split()]

def check(k):
    X = [0] * k
    vis = [False] * k
    for i in range(1, N+1):
        ai = A[i]
        x = ai - A[i-1]

        ix = (i-1) % k
        if not vis[ix]:
            vis[ix] = True
            X[ix] = x
        else:
            if X[ix] != x:
                return False
    return True



ans = []
for i in range(1, N+1):
    if check(i):
        ans.append(i)

print(len(ans))
print(' '.join(map(str, ans)))
