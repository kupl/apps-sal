from collections import deque
N = int(input())
G = [{} for _ in range(N + 1)]
for i in range(N - 1):
    (u, v, w) = map(int, input().split())
    G[u][v] = w
    G[v][u] = w
for i in range(1, N + 1):
    if len(G[i]) == 1:
        start = i
        break


def bfs(s):
    seen = [0 for i in range(N + 1)]
    d = [0 for i in range(N + 1)]
    todo = deque([])
    now = s
    seen[now] = 1
    todo.append(now)
    while 1:
        if len(todo) == 0:
            break
        a = todo.popleft()
        for b in G[a]:
            if seen[b] == 0:
                seen[b] = 1
                todo.append(b)
                d[b] += d[a] + G[a][b]
    return d


d = bfs(start)
for i in range(1, N + 1):
    d_ = d[i]
    if d_ % 2 == 0:
        print(0)
    else:
        print(1)
