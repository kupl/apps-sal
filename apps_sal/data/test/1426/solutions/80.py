import heapq
import sys
input = sys.stdin.readline
(n, m) = map(int, input().split())
INF = 10 ** 18
edge = [[] for i in range(n)]
for i in range(m):
    (x, y) = map(int, input().split())
    edge[x - 1].append(y - 1)
(s, t) = map(int, input().split())


def dijkstra_heap(s, g, p):
    d = [[INF] * p for i in range(n)]
    used = [[True] * p for i in range(n)]
    used[s][0] = False
    ed_list = []
    for es in edge[s]:
        heapq.heappush(ed_list, [1, es, 1])
    while len(ed_list):
        (ken, v, md) = heapq.heappop(ed_list)
        if not used[v][md]:
            continue
        d[v][md] = ken
        used[v][md] = False
        if not used[g][0]:
            break
        for e in edge[v]:
            if used[e][(md + 1) % p]:
                if (md + 1) % p == 1:
                    heapq.heappush(ed_list, [ken + 1, e, 1])
                else:
                    heapq.heappush(ed_list, [ken, e, (md + 1) % p])
    return d[g][0]


ans = dijkstra_heap(s - 1, t - 1, 3)
if ans == INF:
    print(-1)
else:
    print(ans)
