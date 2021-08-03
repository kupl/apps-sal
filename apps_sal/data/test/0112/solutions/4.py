
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
created by shhuan at 2017/11/4 00:13

"""

N = int(input())

A = []
for i in range(N):
    A.append([int(x) for x in input().split()])


def dfs(A, index, p):
    if index >= len(A):
        v = 0
        for u in p:
            v *= 10
            v += u
        return {v}

    ans = set()
    for v in A[index]:
        ans |= dfs(A, index + 1, p + [v])
    ans |= dfs(A, index + 1, p)

    return ans


allNums = set()
for a in itertools.permutations(A, len(A)):
    allNums |= dfs(a, 0, [])

ans = 0
for i in range(1, max(allNums) + 1):
    if i not in allNums:
        break
    ans = i

print(ans)
