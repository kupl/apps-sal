from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline
(n, m, k) = list(map(int, input().split()))
edges = defaultdict(list)
dist = [float('inf')] * (n + 1)
dist[1] = 0
pq = []
for i in range(m):
    (x, y, w) = list(map(int, input().split()))
    edges[x].append((i + 1, y, w))
    edges[y].append((i + 1, x, w))
pq = [(0, 1, -1)]
res = []
c = 0
while pq:
    (v, min_e, min_i) = heapq.heappop(pq)
    if dist[min_e] == v:
        if min_i != -1:
            res.append(min_i)
            c += 1
        if c >= n - 1 or c == k:
            break
        for item in edges[min_e]:
            (i, adj, w) = item
            if dist[min_e] + w < dist[adj]:
                dist[adj] = dist[min_e] + w
                heapq.heappush(pq, (dist[adj], adj, i))
print(len(res))
if k > 0:
    print(' '.join(map(str, res)))
