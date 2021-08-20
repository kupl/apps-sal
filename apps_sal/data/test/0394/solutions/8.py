import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
'\ncreated by shhuan at 2018/10/20 22:37\n\n'
'\n# Definition for a Node.\n'
N = int(input())
A = [0] + [int(x) for x in input().split()]


def check(k):
    X = [0] * k
    vis = [False] * k
    for i in range(1, N + 1):
        ai = A[i]
        x = ai - A[i - 1]
        ix = (i - 1) % k
        if not vis[ix]:
            vis[ix] = True
            X[ix] = x
        elif X[ix] != x:
            return False
    return True


ans = []
for i in range(1, N + 1):
    if check(i):
        ans.append(i)
print(len(ans))
print(' '.join(map(str, ans)))
