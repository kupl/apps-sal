from collections import deque
(n, m) = list(map(int, input().split()))
graph = [[[] for _ in range(3)] for _ in range(n + 1)]
for _ in range(m):
    (u, v) = list(map(int, input().split()))
    graph[u][0].append([v, 1])
    graph[u][1].append([v, 2])
    graph[u][2].append([v, 0])
(s, t) = list(map(int, input().split()))
q = deque([[s, 0]])
visited = [[False] * 3 for _ in range(n + 1)]
visited[s][0] = True
dist = [[-3] * 3 for _ in range(n + 1)]
dist[s][0] = 0
while q:
    (num, cnt) = q.popleft()
    for (i, j) in graph[num][cnt]:
        if visited[i][j]:
            continue
        q.append([i, j])
        visited[i][j] = True
        dist[i][j] = dist[num][cnt] + 1
print(dist[t][0] // 3)
