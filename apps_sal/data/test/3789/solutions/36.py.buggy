from collections import deque
import sys
sys.setrecursionlimit(200000)
n = int(input())
houseki = list(map(int, input().split()))
g = [[] for i in range(n + 2)]
INF = float("inf")
MAX = 0
for i in range(n):
    if houseki[i] <= 0:
        g[0].append([i + 1, -houseki[i], len(g[i + 1])])
        g[i + 1].append([0, 0, len(g[0]) - 1])
    else:
        g[n + 1].append([i + 1, 0, len(g[i + 1])])
        g[i + 1].append([n + 1, houseki[i], len(g[n + 1]) - 1])
        MAX += houseki[i]
    j = (i + 1) * 2
    while j <= n:
        g[i + 1].append([j, INF, len(g[j])])
        g[j].append([i + 1, 0, len(g[i + 1]) - 1])
        j += i + 1


def bfs(s, t):
    nonlocal level
    que = deque([s])
    level[s] = 0
    while que:
        v = que.popleft()
        lv = level[v] + 1
        for y, cap, rev in g[v]:
            if cap and level[y] is None:
                level[y] = lv
                que.append(y)
    return level[t] if level[t] else 0


def dfs(x, t, f):
    if x == t:
        return f
    for j in range(it[x], len(g[x])):
        it[x] = j
        y, cap, rev = g[x][j]
        if cap and level[x] < level[y]:
            d = dfs(y, t, min(f, cap))
            if d:
                g[x][j][1] -= d
                g[y][rev][1] += d
                return d
    return 0


flow = 0
f = INF = float("inf")
level = [None] * (n + 2)
while bfs(0, n + 1):
    it = [0] * (n + 2)
    f = INF
    while f:
        f = dfs(0, n + 1, INF)
        flow += f
    level = [None] * (n + 2)
print(MAX - flow)
