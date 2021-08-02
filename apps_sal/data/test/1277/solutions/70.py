from collections import deque
n, u, v = map(int, input().split())
u -= 1; v -= 1
ki = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    ki[a - 1].append(b - 1)
    ki[b - 1].append(a - 1)
ha = []
for i in range(n):
    if len(ki[i]) == 1:
        ha.append(i)
ta = [0] * n
ao = [0] * n
d = deque()
d.append(u)
visited = [False] * n
visited[u] = True
while d:
    g = d.popleft()
    for i in ki[g]:
        if visited[i]:
            continue
        d.append(i)
        visited[i] = True
        ta[i] = ta[g] + 1
d = deque()
d.append(v)
visited = [False] * n
visited[v] = True
while d:
    g = d.popleft()
    for i in ki[g]:
        if visited[i]:
            continue
        d.append(i)
        visited[i] = True
        ao[i] = ao[g] + 1
if u in ha and ki[u][0] == v:
    print(0)
    return
m = 0
for i in ha:
    if ta[i] < ao[i]:
        m = max(m, ao[i])
print(m - 1)
