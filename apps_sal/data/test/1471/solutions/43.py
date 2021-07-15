from collections import deque

def bfs(s):
    nonlocal color
    q = deque()
    q.append(s)
    color[s] = 0
    while q:
        i = q.popleft()
        for g in G[i]:
            if color[g[0]] == -1:
                if g[1] % 2 == 0:
                    color[g[0]] = color[i]
                else:
                    color[g[0]] = 1 - color[i]
                q.append(g[0])
    return

n = int(input())
G = [[] for _ in range(n + 1)]
color = [-1] * (n + 1)
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    G[u].append([v, w])
    G[v].append([u, w])
bfs(1)
for i in range(1, n + 1):
    print(color[i])
