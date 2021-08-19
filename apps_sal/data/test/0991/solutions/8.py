import sys
from heapq import heappush, heappop
import numpy as np


def input():
    return sys.stdin.readline().rstrip()


def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(mi())


def main():

    def dijkstra(xs, ss):

        def push(v, s, x):
            if s < 0:
                return
            if dist[v, s] <= x:
                return
            dist[v, s] = x
            heappush(que, (x, v, s))
        inf = 10 ** 18
        dist = np.full((n, MAX_S + 1), inf, dtype=int)
        que = []
        push(xs, ss, 0)
        while que:
            (x, v, s) = heappop(que)
            if dist[v, s] < x:
                continue
            ns = min(s + c[v], MAX_S)
            push(v, ns, x + d[v])
            for (nv, a, b) in adj[v]:
                push(nv, s - a, x + b)
        return np.min(dist, axis=1)
    (n, m, s) = mi()
    adj = [[] for i in range(n)]
    MAX_S = 0
    for i in range(m):
        (u, v, a, b) = mi()
        u -= 1
        v -= 1
        adj[u].append((v, a, b))
        adj[v].append((u, a, b))
        MAX_S = max(MAX_S, a)
    MAX_S *= n - 1
    s = min(s, MAX_S)
    (c, d) = ([0] * n, [0] * n)
    for i in range(n):
        (c[i], d[i]) = mi()
    ans = dijkstra(0, s)
    print(*ans[1:], sep='\n')


def __starting_point():
    main()


__starting_point()
