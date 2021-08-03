# ダイクストラ
# 単一始点最短経路(正の辺のみ)
# s=始点 n=頂点数 edgeは隣接リスト(edge=[[[1,2],[2,4]],[[2,1]],[]])
# 0-indexed
from heapq import heappop, heappush


def dijkstra(s, n, edge):
    inf = 10**20
    ans = [inf] * n
    ans[s] = 0
    h = [[0, s]]
    while h:
        c, v = heappop(h)
        if ans[v] < c:
            continue
        for u, t in edge[v]:
            if c + t < ans[u]:
                ans[u] = c + t
                heappush(h, [c + t, u])
    return ans


n, m = list(map(int, input().split()))
edge = [[]for _ in range(n * 3)]
for _ in range(m):
    u, v = list(map(int, input().split()))
    u -= 1
    v -= 1
    edge[u * 3].append([v * 3 + 1, 1])
    edge[u * 3 + 1].append([v * 3 + 2, 1])
    edge[u * 3 + 2].append([v * 3, 1])
s, t = list(map(int, input().split()))
s -= 1
t -= 1
dij = dijkstra(s * 3, n * 3, edge)
if dij[t * 3] == 10**20:
    print((-1))
else:
    print((dij[t * 3] // 3))
