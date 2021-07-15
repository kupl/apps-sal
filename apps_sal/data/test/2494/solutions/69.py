K = int(input())

import heapq
def dijkstra(adj, n, start):
    dj = [10**6] * (n + 1)
    dj[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        fc, fn = heapq.heappop(q)
        if dj[fn] < fc: continue
        for tn, lc in adj[fn]:
            if dj[tn] > dj[fn] + lc:
                dj[tn] = dj[fn] + lc
                heapq.heappush(q, (dj[tn], tn))
    return dj

adj = {}
for i in range(K):
    t = adj.setdefault(i, [])
    t.append(((i + 1) % K, 1))
    t.append(((i * 10) % K, 0))

costs = dijkstra(adj, K - 1, 1)
print(costs[0] + 1)
