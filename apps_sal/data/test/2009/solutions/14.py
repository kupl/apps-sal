import sys
sys.setrecursionlimit(536870912)


def dfs(i, j, vis, g, c):
    vis[i][j] = 1
    c.append((i, j))
    '\n\tif i>0 and \n\t\tif j>0 and vis[i-1][j-1]==0:\n\t\t\tdfs(i-1,j-1,vis,g,c)\n\t\tif j<n-1 and vis[i-1][j+1]==0:\n\t\t\t\tdfs(i-1,j+1,vis,g,c)\n\tif i>0 and j<n-1 and vis[i-1][j+1]==0:\n\t\tdfs(i-1,j+1,vis,g,c)\n\tif i<n-1 and j>0 and vis[i+1][j-1]==0:\n\t\tdfs(i+1,j-1,vis,g,c)\n\tif i<n-1 and j<n-1 and vis[i+1][j+1]==0:\n\t\tdfs(i+1,j+1,vis,g,c)\n\t'
    if i > 0 and vis[i - 1][j] == 0 and (g[i - 1][j] == '0'):
        dfs(i - 1, j, vis, g, c)
    if i < n - 1 and vis[i + 1][j] == 0 and (g[i + 1][j] == '0'):
        dfs(i + 1, j, vis, g, c)
    if j < n - 1 and vis[i][j + 1] == 0 and (g[i][j + 1] == '0'):
        dfs(i, j + 1, vis, g, c)
    if j > 0 and vis[i][j - 1] == 0 and (g[i][j - 1] == '0'):
        dfs(i, j - 1, vis, g, c)


n = int(input())
(r1, c1) = map(int, input().split())
r1 -= 1
c1 -= 1
(r2, c2) = map(int, input().split())
r2 -= 1
c2 -= 1
g = []
for i in range(n):
    g.append(input())
vis = [[0 for i in range(n)] for i in range(n)]
com1 = []
dfs(r1, c1, vis, g, com1)
com2 = []
dfs(r2, c2, vis, g, com2)
m = 1000000000000
for i in com1:
    for j in com2:
        d = (i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2
        m = min(m, d)
print(m)
