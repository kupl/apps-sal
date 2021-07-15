import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

edges = [[] for _ in range(N)]
for _ in range(M):
    l, r, d = map(int, sys.stdin.readline().split())
    edges[l-1].append((r-1, d))
    edges[r-1].append((l-1, -d))

visited = {}
# その人へのパスが複数あり、距離が異なる場合は矛盾
for i in range(N):
    if i in visited:
        continue

    # 連結グラフごとに相対的な距離を決定
    # dist = [0 for _ in range(N)]
    q = deque([(i, 0)])
    while q:
        l, c = q.popleft()
        if l in visited:
            if visited[l] != c:
                print("No")
                return
            continue
        
        visited[l] = c
        # dist[l] = c

        for r, nd in edges[l]:
            q.append((r, c+nd))
    # print(dist)

print("Yes")
