import sys
from collections import deque
input = sys.stdin.readline
(N, M) = map(int, input().split())
edges = [[] for _ in range(N)]
edge_set = set()
for _ in range(M):
    (a, b) = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)
    edge_set.add((a, b))
ans = 0
for (a, b) in edge_set:
    q = deque()
    q.append(0)
    visited = set()
    while q:
        p = q.popleft()
        if p in visited:
            continue
        visited.add(p)
        for np in edges[p]:
            if (p, np) == (a, b) or (np, p) == (a, b):
                continue
            q.append(np)
    if len(visited) != N:
        ans += 1
print(ans)
