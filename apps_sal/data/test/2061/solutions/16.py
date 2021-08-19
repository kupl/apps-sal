import sys
from collections import defaultdict, OrderedDict

sys.setrecursionlimit(10**5)
n, m, k = list(map(int, input().split()))

g = []
for i in range(n):
    g.append(list(input()))

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
d = defaultdict(list)


def dfs(g, u, visited):
    visited[u[0]][u[1]] = True
    # print(visited)

    for i in range(4):
        y = u[0] + dy[i]
        x = u[1] + dx[i]
        # print('y = {0} x = {1}'.format(y, x))
        if y >= 0 and y < n and x >= 0 and x < m \
           and g[y][x] == '.' and not visited[y][x]:
            # if u == (2, 3):
            # print('y = {0} x = {1}'.format(y, x))
            dfs(g, (y, x), visited)


def dfs_(g, u, visited, component):
    visited[u[0]][u[1]] = True
    d[component].append(u)

    for i in range(4):
        y = u[0] + dy[i]
        x = u[1] + dx[i]
        if y >= 0 and y < n and x >= 0 and x < m \
           and g[y][x] == '.' and not visited[y][x]:
            dfs_(g, (y, x), visited, component)


# dfs from the outer edge and mark the bad ones
visited = [[False for j in range(m)] for i in range(n)]

for i in range(m):
    if g[0][i] == '.' and not visited[0][i]:
        dfs(g, (0, i), visited)
    if g[n - 1][i] == '.' and not visited[-1][i]:
        dfs(g, (n - 1, i), visited)

for i in range(1, n - 1):
    if g[i][0] == '.' and not visited[i][0]:
        dfs(g, (i, 0), visited)
    if g[i][m - 1] == '.' and not visited[i][m - 1]:
        dfs(g, (i, m - 1), visited)

component = 0
for i in range(1, n - 1):
    for j in range(1, m - 1):
        if g[i][j] == '.' and not visited[i][j]:
            dfs_(g, (i, j), visited, component)
            component += 1


# print(d)
l = sorted(list(d.items()), key=lambda x: len(x[1]))

i = 0
count = 0
while component > k:
    component -= 1
    count += len(l[i][1])
    for u in l[i][1]:
        g[u[0]][u[1]] = '*'
    i += 1

print(count)

for i in range(n):
    print(''.join(g[i]))
