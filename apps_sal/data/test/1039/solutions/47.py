from collections import deque

N = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

Q, K = map(int, input().split())

visited = [-1 for _ in range(N + 1)]

visited[K] = 0
que = deque()
que.append(K)

while (len(que)):
    now = que.popleft()

    for nxt, c in graph[now]:
        if(visited[nxt] != -1):
            continue
        visited[nxt] = visited[now] + c
        que.append(nxt)

for i in range(Q):
    x, y = map(int, input().split())
    print(visited[x] + visited[y])
