# coding=utf-8
import sys

sys.setrecursionlimit(10000)
g = []

n, m = list(map(int, input().split()))
idx = [[False for i in range(m)] for j in range(n)]
for k in range(n):
    g.append(input())


def dfs(i, j, li, lj):
    idx[i][j] = True
    if i + 1 < n and g[i][j] == g[i + 1][j]:
        if idx[i + 1][j] is False:
            return dfs(i + 1, j, i, j)
        elif not (li == i and lj == j) and i + 1 != li:
            return 'Yes'
    if i - 1 >= 0 and g[i][j] == g[i - 1][j]:
        if idx[i - 1][j] is False:
            return dfs(i - 1, j, i, j)
        elif not (li == i and lj == j) and i - 1 != li:
            return 'Yes'
    if j - 1 >= 0 and g[i][j] == g[i][j - 1]:
        if idx[i][j - 1] is False:
            return dfs(i, j - 1, i, j)
        elif not (li == i and lj == j) and j - 1 != lj:
            return 'Yes'
    if j + 1 < m and g[i][j] == g[i][j + 1]:
        if idx[i][j + 1] is False:
            return dfs(i, j + 1, i, j)
        elif not (li == i and lj == j) and j + 1 != lj:
            return 'Yes'
    return None


for i in range(n):
    for j in range(m):
        if not idx[i][j]:
            ans = dfs(i, j, i, j)
            if ans:
                print(ans)
                break
    else:
        continue
    break
else:
    print('No')
