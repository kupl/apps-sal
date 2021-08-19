import sys


def get_array():
    return list(map(int, sys.stdin.readline().split()))


def get_ints():
    return map(int, sys.stdin.readline().split())


def input():
    return sys.stdin.readline().strip('\n')


visited = []
out = []
for i in range(1010):
    visited.append([])
    out.append([])
    for j in range(1010):
        visited[i].append(0)
        out[i].append(-1)


def dfs(x, y):
    cells = []
    c = 0
    Q = [(x, y)]
    while Q:
        (x, y) = Q.pop()
        if x >= n or x < 0 or y >= m or (y < 0):
            return
        if l[x][y] == '*':
            c += 1
            continue
        if visited[x][y]:
            continue
        visited[x][y] = 1
        cells.append((x, y))
        Q.append((x + 1, y))
        Q.append((x - 1, y))
        Q.append((x, y + 1))
        Q.append((x, y - 1))
    for x in cells:
        if visited[x[0]][x[1]] and out[x[0]][x[1]] == -1:
            out[x[0]][x[1]] = c


(n, m, k) = get_ints()
l = []
for i in range(n):
    l.append(input())
for i in range(n):
    for j in range(m):
        if not visited[i][j] and l[i][j] == '.':
            dfs(i, j)
for i in range(k):
    (x, y) = get_ints()
    (x, y) = (x - 1, y - 1)
    ans = out[x][y]
    print(ans)
