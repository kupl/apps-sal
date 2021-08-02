import itertools
import bisect
import copy
import sys
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush, heapify


def bfs_01(v, mod):
    q = deque(); q.append(v)
    visited = [False] * mod
    cur = 0
    while cur == 0:
        s, x = q.popleft()
        if visited[x]:
            continue
        visited[x] = True
        if x == 0:
            cur = s
            return cur
        q.appendleft((s, (10 * x) % mod))
        q.append((s + 1, (x + 1) % mod))


def examD():
    K = I()
    ans = bfs_01((1, 1), K)
    print(ans)


def I(): return int(sys.stdin.readline())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()


mod = 10**9 + 7
inf = float('inf')

examD()
