from collections import defaultdict
import heapq
graph = defaultdict(set)
(n, m) = map(int, input().split())
for _ in range(m):
    (a, b) = map(int, input().split())
    if a != b:
        graph[a].add(b)
        graph[b].add(a)
seen = {1}
hist = [1]
h = list(graph[1])
heapq.heapify(h)
while len(hist) < n:
    next_node = heapq.heappop(h)
    if next_node in seen:
        continue
    seen.add(next_node)
    hist.append(next_node)
    for node in graph[next_node]:
        heapq.heappush(h, node)
print(' '.join((str(x) for x in hist)))
