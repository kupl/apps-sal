from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
dist = [0] * (n + 1)
visited = [0] * (n + 1)


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

root = 1
visited[root] = 1
d = deque([root])

while d:
    v = d.popleft()
    for i in graph[v]:
        if visited[i]:
            continue
        visited[i] = 1
        dist[i] = v
        d.append(i)

print('Yes')
ans = dist[2:]
print(*ans, sep="\n")
