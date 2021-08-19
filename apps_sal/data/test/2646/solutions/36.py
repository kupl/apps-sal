from collections import deque
(N, M) = map(int, input().split())
G = [[] for _ in range(N + 1)]
m = [tuple(map(int, input().split())) for _ in range(M)]
for (a, b) in m:
    G[a].append(b)
    G[b].append(a)
par = [0] * (N + 1)
visited = [0] * (N + 1)
root = 1
visited[root] = 1
q = deque([root])
while q:
    v = q.popleft()
    for w in G[v]:
        if visited[w]:
            continue
        visited[w] = 1
        par[w] = v
        q.append(w)
print('Yes')
print(*par[2:], sep='\n')
