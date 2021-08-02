from collections import defaultdict, deque
import sys
import heapq
import bisect
import math
import itertools
import string
import queue
import datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9 + 7
eps = 10**-7
def inpl(): return list(map(int, input().split()))
def inpl_s(): return list(input().split())


N = int(input())
LRs = []
L1 = L2 = 0
R1 = R2 = INF

for i in range(N):
    L, R = inpl()
    if L2 <= L:
        L1 = L2
        L2 = L
    elif L1 < L < L2:
        L1 = L

    if R <= R2:
        R1 = R2
        R2 = R
    elif R2 < R < R1:
        R1 = R

    LRs.append([L, R])

ans = 0
for L, R in LRs:
    if L == L2:
        tmpL = L1
    else:
        tmpL = L2

    if R == R2:
        tmpR = R1
    else:
        tmpR = R2

    ans = max(ans, tmpR - tmpL)

print(ans)
