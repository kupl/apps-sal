import sys
sys.setrecursionlimit(10000)


def f(i, j):
    return -1 < i < n and -1 < j < m


def dfs(c, r, l):
    used[c][r] = 1
    for (i, j) in {(0, 1), (-1, 0), (1, 0), (0, -1)}:
        if f(c + i, r + j) and a[c + i][r + j] == a[c][r]:
            if used[c + i][r + j] == 0:
                prev[c + i][r + j] = (c, r)
                dfs(c + i, r + j, l + 1)
            elif used[c + i][r + j] == 1 and prev[c][r] != (c + i, r + j):
                nonlocal s
                s = "Yes"
    used[i][j] = 2


n, m = map(int, input().split())
a = []
s = "No"
for i in range(n):
    a.append(list(input().rstrip()))

used = [[0 for i in range(m)] for i in range(n)]
prev = [[-1 for i in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        if used[i][j] == 0:
            dfs(i, j, 0)
print(s)
