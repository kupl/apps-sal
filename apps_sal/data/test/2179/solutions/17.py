import heapq
from sys import stdin
from math import inf
input = stdin.readline


def put():
    return list(map(int, input().split()))


def dijkstra(u):
    q = [(0, 0, u - 1, 0)]
    vis = [False] * n
    ans = 0
    res = []
    while q:
        _, k, i, f = heapq.heappop(q)
        if vis[i]:
            continue
        vis[i] = True
        ans += k
        res.append(f)
        for w, j, f in graph[i]:
            if not vis[j]:
                heapq.heappush(q, (_ + w, w, j, f))

    print(ans)
    res = res[1:]
    print(*res)


n, m = put()
graph = [[] for _ in range(n)]
for _ in range(m):
    x, y, z = put()
    x, y = x - 1, y - 1
    graph[x].append((z, y, _ + 1))
    graph[y].append((z, x, _ + 1))
d = int(input())
dijkstra(d)
