from heapq import heappop, heappush
import sys
N, M = map(int, input().split())
edges = [[] for _ in [0] * N]
for u, v in (map(int, l.split()) for l in sys.stdin):
    edges[u - 1].append(v - 1)
    edges[v - 1].append(u - 1)

visited = [0] * N
ans = []
heap = [0]
ans_append = ans.append

while heap:
    v = heappop(heap)
    visited[v] = 1
    ans_append(v + 1)

    edges[v].sort()
    for to_v in edges[v]:
        if visited[to_v]:
            continue
        visited[to_v] = 1
        heappush(heap, to_v)

print(*ans)
