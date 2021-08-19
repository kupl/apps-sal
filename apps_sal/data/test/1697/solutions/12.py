import sys


def dfs(i, j, vis, out, mapp, s=2):
    if vis[i][j] and vis[i][j] != s - 1:
        return True
    t = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    vis[i][j] = s
    out[i][j] = True
    for k in t:
        try:
            (u, v) = (k[0] + i, k[1] + j)
            if u < 0 or v < 0:
                continue
            if vis[u][v] != s - 1 and mapp[u][v] == mapp[i][j] and dfs(u, v, vis, out, mapp, s + 1):
                return True
        except Exception:
            pass
    vis[i][j] = 0
    return False


sys.setrecursionlimit(2500)
(n, m) = input().split()
(n, m) = (int(n), int(m))
exist = set()
mapp = [0 for i in range(n)]
for i in range(n):
    mapp[i] = input()
for i in range(n):
    for j in range(m):
        exist.add(mapp[i][j])
key = 0
t = [(0, 1), (1, 0), (-1, 0), (0, -1)]
out = [[False for i in range(m)] for j in range(n)]
for c in exist:
    if key:
        break
    vis = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        if key:
            break
        for j in range(m):
            if key:
                break
            if mapp[i][j] == c and (not out[i][j]) and dfs(i, j, vis, out, mapp):
                key = 1
                break
if key:
    print('Yes')
else:
    print('No')
