from collections import defaultdict
import heapq
n = int(input())
graph = defaultdict(set)
for x in range(n - 1):
    (a, b) = map(int, input().split())
    graph[a].add((x, b))
    graph[b].add((x, a))
order = []
seen = set()
start = 1
q = list(graph[start])
heapq.heapify(q)
while q:
    (t, node) = heapq.heappop(q)
    if node in seen:
        continue
    seen.add(node)
    order.append(node)
    for neighbor in graph[node]:
        heapq.heappush(q, neighbor)
print(*order)
