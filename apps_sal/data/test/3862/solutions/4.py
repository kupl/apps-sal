from collections import deque
(n, k) = list(map(int, input().split()))
conc = set((int(x) - n for x in input().split()))
q = deque()
q.append(0)
visited = {i: False for i in range(-1000, 1001)}
dist = {i: 0 for i in range(-1000, 1001)}
ans = -1
visited[0] = True
found = False
while q:
    u = q.popleft()
    for c in conc:
        v = c + u
        if v == 0:
            ans = dist[u] + 1
            found = True
            break
        if v <= 1000 and v >= -1000 and (not visited[v]):
            visited[v] = True
            dist[v] = dist[u] + 1
            q.append(v)
    if found:
        break
print(ans)
