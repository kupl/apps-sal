from collections import deque

n, m = list(map(int, input().split()))
graph = [[] for i in range(n)]
for i in range(m):
    u, v = list(map(int, input().split()))
    u -= 1
    v -= 1
    graph[u].append([i,v])
    graph[v].append([i,u])
    
cnt = 0
for i in range(m):
    d = deque()
    d.append(0)
    visited = [False]*n
    visited[0] = True
    while d:
        cf = d.pop()
        for ci, ct in graph[cf]:
            if ci == i:
                continue
            if not visited[ct]:
                d.append(ct)
                visited[ct] = True
    if False in visited:
        cnt += 1
print(cnt)

