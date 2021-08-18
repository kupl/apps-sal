from collections import deque
import sys
import io
import os
input = sys.stdin.buffer.readline

n, m = map(int, input().split())
g = [[] for _ in range(n)]
edge = []
for i in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    g[a].append(b)
    edge.append((a, b))

INF = 10**18
temp = INF
for a, b in edge:
    q = deque([])
    q.append(b)
    visit = [INF] * n
    visit[b] = 0
    par = [-1] * n
    while q:
        v = q.popleft()
        for u in g[v]:
            if visit[u] == INF:
                visit[u] = visit[v] + 1
                par[u] = v
                q.append(u)
    if visit[a] + 1 <= temp:
        ans = []
        v = a
        ans.append(v + 1)
        while par[v] != -1:
            v = par[v]
            ans.append(v + 1)
        temp = visit[a] + 1

if temp == INF:
    print(-1)
else:
    if ans:
        print(len(ans))
        print(*ans, sep='\n')
    else:
        print(-1)
