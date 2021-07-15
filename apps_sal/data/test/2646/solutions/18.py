from collections import deque

n,m = map(int,input().split())
to = [[] for _ in range(n)]

for i in range(m):
    x, y = map(int,input().split())
    to[x-1].append(y-1)
    to[y-1].append(x-1)

INF = float('inf')
dist = [INF]*n
dist[0] = 0

pre = [-1]*n

que = deque([])
que.append(0)

while que:
    v = que.popleft()
    for u in to[v]:
        if dist[u] != INF:continue
        dist[u] = v + 1
        pre[u] = v
        que.append(u)
print("Yes")
for i in range(1,n):
    print(dist[i])
