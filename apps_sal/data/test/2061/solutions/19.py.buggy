from sys import setrecursionlimit
def corr(x, y): return 0 <= x < n and 0 <= y < m and a[x][y] == '.'
def ocean(x, y): return x in (0, n - 1) or y in (0, m - 1)


D = (0, 1), (0, -1), (1, 0), (-1, 0)
setrecursionlimit(10 ** 5)


def dfs(x, y):
    nonlocal size, flag
    was[x][y] = clr
    size += 1
    if ocean(x, y):
        flag = True
    for dx, dy in D:
        nx, ny = x + dx, y + dy
        if corr(nx, ny) and not was[nx][ny]:
            dfs(nx, ny)


def read(): return map(int, input().split())


n, m, k = read()
a = [input() for i in range(n)]
s = []
was = [[0] * m for i in range(n)]
clr = 1
for i in range(n):
    for j in range(m):
        if not was[i][j] and a[i][j] == '.':
            flag = False
            size = 0
            dfs(i, j)
            if not flag:
                s.append((size, clr))
            clr += 1
s.sort()
ans = 0
color = set()
for i in range(len(s) - k):
    ans += s[i][0]
    color.add(s[i][1])
b = [list(a[i]) for i in range(n)]
for i in range(n):
    for j in range(m):
        if was[i][j] in color:
            b[i][j] = '*'
print(ans)
[print(''.join(i)) for i in b]
