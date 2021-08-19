from collections import deque
n, u, v = map(int, input().split())
edge = [[] for i in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)
visitedu = [-1] * n
visitedv = [-1] * n


def bfs(s, visited):
    q = deque([s])
    visited[s] = 0
    while q:
        x = q.popleft()
        for nx in edge[x]:
            if visited[nx] == -1:
                visited[nx] = visited[x] + 1
                q.append(nx)
    return


bfs(u - 1, visitedu)
bfs(v - 1, visitedv)
a = 0
b = 10**10
for i in range(n):
    if visitedu[i] < visitedv[i]:
        a = max(a, visitedv[i])
    elif visitedu[i] == visitedv[i]:
        b = min(b, visitedv[i])
# print(visitedv)
# print(visitedu)
if b == 10**10:
    b = -1
if a <= b:
    print(b)
else:
    print(a - 1)
