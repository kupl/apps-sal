import sys
from collections import deque

N = int(sys.stdin.readline())

edges = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b, c = map(int, sys.stdin.readline().split())
    edges[a - 1].append((b - 1, c))
    edges[b - 1].append((a - 1, c))

Q, K = map(int, sys.stdin.readline().split())

# Kを始点とする、各点までの距離
dist = [-1 for _ in range(N)]

visited = set()
q = deque([(K - 1, 0)])
while q:
    p, c = q.popleft()
    if p in visited:
        continue
    dist[p] = c

    visited.add(p)
    for (next_p, next_c) in edges[p]:
        q.append((next_p, c + next_c))
# print(dist)

for _ in range(Q):
    x, y = map(int, sys.stdin.readline().split())
    print(dist[x - 1] + dist[y - 1])
