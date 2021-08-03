import bisect
import collections
import copy
import heapq
import itertools
import math
import numpy
import string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())


N = I()
P = [0] + LI()
ind = {i: 0 for i in range(1, N)}
for i, p in enumerate(P[1:], 1):
    ind[p] = i
ans = []
set_ans = set()
for i in range(1, N + 1):
    if ind[i] == i:
        continue
    while 1:
        ind_i = ind[i]
        P[ind_i], P[ind_i - 1] = P[ind_i - 1], P[ind_i]
        ind[i] = ind_i - 1
        ind[P[ind_i]] = ind_i
        if ind_i - 1 in set_ans:
            print((-1))
            return
        ans.append(ind_i - 1)
        set_ans.add(ind_i - 1)
        if ind[i] == i:
            break
if len(ans) == N - 1:
    for x in ans:
        print(x)
else:
    print((-1))
