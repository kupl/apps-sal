#!/usr/bin/env python3
from collections import *


def ri():
    return list(map(int, input().split()))


d = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def bfs(s, adj, v, l):
    if v[s] == 1:
        return 0
    q = deque()
    q.append(s)
    v[s] = 1
    while q:
        n = q.popleft()
        for a in adj[n]:
            if v[a] == 0:
                for i in range(4):
                    if dv[n][i] == 0:
                        dv[n][i] = 1
                        break
                pos[a][0] = pos[n][0] + d[i][0] * 2**(31 - l[n])
                pos[a][1] = pos[n][1] + d[i][1] * 2**(31 - l[n])
                if i == 0:
                    dv[a][2] = 1
                elif i == 1:
                    dv[a][3] = 1
                elif i == 2:
                    dv[a][0] = 1
                elif i == 3:
                    dv[a][1] = 1
                l[a] = l[n] + 1
                q.append(a)
                v[a] = 1


n = int(input())
adj = [set() for i in range(n)]
v = [0 for i in range(n)]
l = [0 for i in range(n)]
dv = [[0, 0, 0, 0] for i in range(n)]
pos = [[0, 0] for i in range(n)]

for i in range(n - 1):
    a, b = ri()
    a -= 1
    b -= 1
    adj[a].add(b)
    adj[b].add(a)

for i in range(n):
    if len(adj[i]) > 4:
        print("NO")
        return

bfs(0, adj, v, l)

print("YES")
for i in range(n):
    print(pos[i][0], pos[i][1])
