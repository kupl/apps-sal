from collections import defaultdict, deque
import sys
import heapq
import bisect
import math
import itertools
import string
import queue
import copy
import time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9 + 7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())


(m, n, k, T) = list(map(int, input().split()))
a = list(map(int, input().split()))
DD = []
LR = []

for i in range(k):
    L, R, D = map(int, input().split())
    LR.append((L, R))
    DD.append((D, i))
DD.sort()
DD_id = [D for D, i in DD]


def Solve(x):
    idx = bisect.bisect_right(DD_id, x)
    path = [0] * (n + 2)
    for X, i in DD[idx:]:
        LL, RR = LR[i]
        path[LL] += 1
        path[RR + 1] -= 1
    t = n + 1
    bp = path[0]
    for i in range(1, n + 2):
        p = bp + path[i]
        if p > 0:
            t += 2
        bp = p

    return t <= T


L = -1
R = 2 * 10**5 + 2
while R - L > 1:
    mid = (L + R) // 2
    if Solve(mid):
        R = mid
    else:
        L = mid

ans = 0
for i in a:
    if i >= R:
        ans += 1
print(ans)
