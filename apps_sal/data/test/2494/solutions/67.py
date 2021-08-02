from collections import deque

k = int(input())
v = list(range(k))
stack = deque([1])
inf = float('inf')
visited = [0] * k
dist = [inf] * k
dist[1] = 0
while stack:
    v = stack.pop()
    if not visited[v]:
        nv0 = 10 * v % k
        nv1 = (v + 1) % k
        if dist[nv0] > dist[v]:
            dist[nv0] = dist[v]
            stack.append(nv0)
        if dist[nv1] > 1 + dist[v]:
            stack.appendleft(nv1)
            dist[nv1] = dist[v] + 1
        visited[v] = 1
print(dist[0] + 1)
