from fractions import Fraction
import sys
import math
import io
import os
from bisect import bisect_left as bl, bisect_right as br, insort
from heapq import heapify, heappush, heappop
from collections import defaultdict as dd, deque, Counter
def data(): return sys.stdin.readline().strip()
def mdata(): return list(map(int, data().split()))
def outl(var): sys.stdout.write('\n'.join(map(str, var)) + '\n')
def out(var): sys.stdout.write(str(var) + '\n')


INF = float('inf')
mod = int(1e9) + 7


def dfs(graph, start=0):
    n = len(graph)

    dp = [0] * n
    visited, finished = [False] * n, [False] * n
    par = [0] * n

    stack = [start]
    while stack:
        start = stack[-1]

        if not visited[start]:
            visited[start] = True
            for child in graph[start]:
                if not visited[child]:
                    stack.append(child)
                    par[child] = start

        else:
            stack.pop()

            dp[start] += p[start]

            for child in graph[start]:
                if finished[child]:
                    dp[start] += dp[child]

            finished[start] = True

    return dp


def dfs2(graph, start=0):
    n = len(graph)

    dp = [0] * n
    visited, finished = [False] * n, [False] * n
    n = [0] * n

    stack = [start]
    while stack:
        start = stack[-1]

        if not visited[start]:
            visited[start] = True
            for child in graph[start]:
                if not visited[child]:
                    stack.append(child)

        else:
            stack.pop()

            dp[start] += (v[start] + h[start]) // 2
            a = v[start] - dp[start]
            if dp[start] - a != h[start] or a < 0:
                return False

            k = 0
            for child in graph[start]:
                if finished[child]:
                    k += dp[child]
            if k > dp[start]:
                return False

            finished[start] = True

    return True


for t in range(int(data())):
    n, m = mdata()
    p = mdata()
    h = mdata()
    g = [[] for i in range(n)]
    for i in range(n - 1):
        u, v = mdata()
        u, v = u - 1, v - 1
        g[u].append(v)
        g[v].append(u)
    v = dfs(g, 0)
    if dfs2(g, 0):
        out("YES")
    else:
        out("NO")
