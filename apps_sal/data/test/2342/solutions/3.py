from math import *


def r1(t):
    return t(input())


def r2(t):
    return [t(i) for i in input().split()]


def r3(t):
    return [t(i) for i in input()]


g = []


def dfs(i, j, n, m):
    if g[i][j] == '
    return 0
    ans = 0
    if g[i][j] == 'G':
        ans += 1
    if g[i][j] == 'B':
        return -100000
    g[i][j] = '
    if (i > 0):
        ans += dfs(i - 1, j, n, m)
    if (i < n - 1):
        ans += dfs(i + 1, j, n, m)
    if (j > 0):
        ans += dfs(i, j - 1, n, m)
    if (j < m - 1):
        ans += dfs(i, j + 1, n, m)
    return ans


for _ in range(r1(int)):
    n, m = r2(int)
    g = []
    used = []
    for i in range(n):
        g.append(r3(str))

    cnt = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == 'B':
                if (i > 0) and g[i - 1][j] == '.':
                    g[i - 1][j] = '
                if (i < n - 1) and g[i + 1][j] == '.':
                    g[i + 1][j] = '
                if (j > 0) and g[i][j - 1] == '.':
                    g[i][j - 1] = '
                if (j < m - 1) and g[i][j + 1] == '.':
                    g[i][j + 1] = '
            elif g[i][j] == 'G':
                cnt += 1
    if (dfs(n - 1, m - 1, n, m) == cnt):
        print('Yes')
    else:
        print('No')
