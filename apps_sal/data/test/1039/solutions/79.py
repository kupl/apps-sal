import sys
def input(): return sys.stdin.readline().rstrip()
def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(mi())

from collections import deque
from heapq import heappop, heappush
def main():
        

    def dijkstra(k):
        def push(v, x):
            if dist[v] <= x:
                return
            dist[v] = x
            heappush(q, (x, v))

        inf = 10**18
        dist = [inf]*n
        q = []
        push(k, 0)
        while q:
            x, v = heappop(q)
            if x > dist[v]:
                continue
            for nv, c in g[v]:
                push(nv, x+c)
        return dist

    n = ii()
    g = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b, c = mi()
        a -= 1
        b -= 1

        g[a].append((b, c))
        g[b].append((a, c))
    q, k = mi()
    k -= 1
    dist = dijkstra(k)
    for i in range(q):
        a, b = mi()
        a -= 1
        b -= 1
        print(dist[a]+dist[b])


def __starting_point():
    main()
__starting_point()
