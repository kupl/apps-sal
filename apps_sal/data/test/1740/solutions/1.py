n = int(input())
# 2<=n<=150.000
import heapq
from collections import defaultdict
graph = defaultdict(set)
for x in range(n-1):
    a,b = map(int,input().split())
    graph[a].add((x,b))
    graph[b].add((x,a))
#heapq.heapify(a)

order = []
seen = set()
start = 1
q = list(graph[start])
heapq.heapify(q)
while q:
    t, node = heapq.heappop(q)
    if node in seen:continue
    seen.add(node)
    order.append(node)
    for neighbor in graph[node]:
        heapq.heappush(q,neighbor)
print (*order)
