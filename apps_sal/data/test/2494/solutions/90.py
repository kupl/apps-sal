from collections import deque

k = int(input())

visited = [False]*(k+1)
dist = [0]*(k+1)
dist[1] = 1
que = deque([(1, 1)])

while len(que) > 0:
    cost, node = que.popleft()
    if visited[node]:
        continue
    
    visited[node] = True
    dist[node] = cost

    if not visited[10*node%k]:
        que.appendleft((cost, 10*node%k))
    if not visited[(node+1)%k]:
        que.append((cost+1, (node+1)%k))

print((dist[0]))

