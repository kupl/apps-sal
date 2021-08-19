from collections import deque


def bfs(G, s, j):
    q = deque()
    q.append(s)
    visit[s][j] = 1
    p = 1
    while q:
        u = q.popleft()
        for v in G[u]:
            if not visit[v][j]:
                visit[v][j] = 1
                p += 1
                q.append(v)
    return p


(n, k) = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
mod = 998244353
G1 = [[] for _ in range(n)]
G2 = [[] for _ in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        f = 1
        for l in range(n):
            if a[i][l] + a[j][l] > k:
                f = 0
                break
        if f:
            G1[i].append(j)
            G1[j].append(i)
for i in range(n):
    for j in range(i + 1, n):
        f = 1
        for l in range(n):
            if a[l][i] + a[l][j] > k:
                f = 0
                break
        if f:
            G2[i].append(j)
            G2[j].append(i)
ans = 1
visit = [[0] * 2 for _ in range(n + 5)]
factorial = [1] * (n + 5)
for i in range(2, n + 5):
    factorial[i] = factorial[i - 1] * i % mod
for i in range(n):
    if not visit[i][0]:
        p = bfs(G1, i, 0)
        ans *= factorial[p]
        ans %= mod
    if not visit[i][1]:
        p = bfs(G2, i, 1)
        ans *= factorial[p]
        ans %= mod
print(ans)
