from collections import deque


def bfs(v):
    q = deque()
    q.append(v)
    w = []
    while len(q):
        cur = q.popleft()
        w.append(cur)
        p[cur] = c
        for i in g[cur]:
            if p[i] == 0:
                q.append(i)
                p[i] = c
    k.append(w)


n, m = list(map(int, input().split()))

g = [[] for i in range(n + 1)]
p = [0] * (n + 1)
k = [[]]

for i in range(m):
    a, b = list(map(int, input().split()))
    g[a].append(b)
    g[b].append(a)


c = 0
for v in range(1, n + 1):
    if p[v] == 0:
        c += 1
        bfs(v)


ans = 0
for i in range(1, len(k)):
    fl = True
    for j in range(len(k[i])):
        if len(g[k[i][j]]) != 2:
            fl = False
    if fl:
        ans += 1

print(ans)
