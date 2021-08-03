from collections import deque
n = int(input())
ver = list(map(int, input().split()))
adj = [{} for i in range(n)]

for i in range(n - 1):
    p, c = map(int, input().split())
    adj[i + 1][p - 1] = c
    adj[p - 1][i + 1] = c

q = deque([(0, 0, 0)])

sad = [0] * n
vis = [0] * n

while q:
    v, d, md = q.popleft()
    vis[v] = 1

    for nv, nvd in adj[v].items():
        if vis[nv] == 1 and sad[nv] == 1:
            sad[v] = 1

    if d > ver[v] or d - md > ver[v]:
        sad[v] = 1

    for nv, nvd in adj[v].items():
        if vis[nv] == 0:
            q.append((nv, d + nvd, min(d + nvd, md)))

print(sum(sad))
