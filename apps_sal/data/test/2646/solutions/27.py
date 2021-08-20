from heapq import heappush, heapify, heappop


def dijkstra(start: '始点', V: '頂点数', es: '隣接リスト', INF=10000000000):
    prev = [-1] * n
    d = [INF] * n
    que = [start]
    d[start] = 0
    while que:
        (dv, v) = divmod(heappop(que), INF)
        if d[v] < dv:
            continue
        for (e, de) in es[v]:
            if d[e] > d[v] + de:
                d[e] = d[v] + de
                heappush(que, d[e] * INF + e)
                prev[e] = v
    return (d, prev)


def get_path(t, prev):
    path = []
    while t != -1:
        path.append(t)
        t = prev[t]
    path.reverse()
    return path


(n, m) = list(map(int, input().split()))
es = [[] for _ in range(n)]
for i in range(m):
    (a, b) = list(map(int, input().split()))
    (a, b) = (a - 1, b - 1)
    es[a].append((b, 1))
    es[b].append((a, 1))
(d, prev) = dijkstra(0, n, es)
print('Yes')
for i in range(1, n):
    print(prev[i] + 1)
