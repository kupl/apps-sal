import sys
(n, m) = [int(x) for x in input().split()]
field = [''] * n
labels = [[0]] * n
sys.setrecursionlimit(10000)
for i in range(n):
    field[i] = input().strip()
    labels[i] = [0] * m


def is_valid(i, j):
    return 0 <= i < n and 0 <= j < m


def dfs(i, j, p, k, cc=0):
    if labels[i][j] == k:
        return True
    labels[i][j] = k
    res = False
    dd = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    for d in dd:
        if is_valid(i + d[0], j + d[1]) and (i + d[0] != p[0] or j + d[1] != p[1]):
            if field[i + d[0]][j + d[1]] == field[i][j]:
                res = res or dfs(i + d[0], j + d[1], [i, j], k, cc + 1)
    return res


ok = False
k = 1
for i in range(n):
    for j in range(m):
        if labels[i][j] == 0:
            ok = ok or dfs(i, j, [i, j], k)
            k += 1
if ok:
    print('Yes')
else:
    print('No')
