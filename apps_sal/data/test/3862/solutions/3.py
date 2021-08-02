from collections import deque
n, k = list(map(int, input().split()))
d = set(int(x) - n for x in input().split())

q = deque()
q.append(0)

visited = {i: False for i in range(-1000, 1001)}
dist = {i: 0 for i in range(-1000, 1001)}

ans = -1
visited[0] = True
found = False
while q:
    u = q.popleft()
    for i in d:
        if i + u == 0:

            ans = dist[u] + 1
            found = True
            break
        if i + u <= 1000 and i + u >= -1000 and not visited[i + u]:
            visited[i + u] = True
            dist[i + u] = dist[u] + 1
            q.append(i + u)

    if found:
        break

print(ans)
