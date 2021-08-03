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


N, M = inpl()

if M == 0:
    print(-1)
    return

cnts = [0] * N
lines = defaultdict(set)
for _ in range(M):
    a, b = inpl()
    a -= 1
    b -= 1
    cnts[a] += 1
    cnts[b] += 1
    lines[a].add(b)
    lines[b].add(a)

setc = set(cnts)
L = len(setc)
ans = [-1] * N
if L == 1:
    ans[a] = 1
    ans[b] = 2
    for i in range(N):
        if ans[i] != 0:
            if i not in lines[a]:
                ans[i] = 1
            elif i not in lines[b]:
                ans[i] = 2
            else:
                ans[i] = 3
elif L == 2:
    c1, c2 = list(setc)
    if c1 * 2 + c2 == N * 2:
        i1 = cnts.index(c1)
        i2 = cnts.index(c2)
        for i, c in enumerate(cnts):
            if c == c2:
                ans[i] = 2
            else:
                if i not in lines[i1]:
                    ans[i] = 1
                else:
                    ans[i] = 3
    elif c1 + c2 * 2 == N * 2:
        i1 = cnts.index(c1)
        i2 = cnts.index(c2)
        for i, c in enumerate(cnts):
            if c == c1:
                ans[i] = 1
            else:
                if i not in lines[i2]:
                    ans[i] = 2
                else:
                    ans[i] = 3
    else:
        print(-1)
        return
elif L == 3:
    c1, c2, c3 = list(setc)
    for i, c in enumerate(cnts):
        if c == c1:
            ans[i] = 1
        elif c == c2:
            ans[i] = 2
        elif c == c3:
            ans[i] = 3
else:
    print(-1)
    return


if len(set(ans)) != 3:
    print(-1)
    return

for s in range(N):
    for t in lines[s]:
        if ans[s] == ans[t]:
            print(-1)
            return

print(' '.join(map(str, ans)))
