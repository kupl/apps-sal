import sys
def dfs(i, j):
    nonlocal used, ans
    used[i][j] = True
    ans.append((i, j))
    if (i - 1 >= 0 and j >= 0 and not used[i - 1][j]):
        dfs(i - 1, j)
    if (i >= 0 and j + 1 <= m - 1 and not used[i][j + 1]):
        dfs(i, j + 1)  
    if (i + 1 <= n - 1 and j <= m - 1 and not used[i + 1][j]):
        dfs(i + 1, j)
    if (i <= n - 1 and j - 1 >= 0 and not used[i][j - 1]):
        dfs(i, j - 1)


sys.setrecursionlimit(1000000)
n, m, k = map(int, input().split())
used = [[True for i in range(m)] for j in range(n)]
hole = [[True for i in range(m)] for j in range(n)]
for i in range(n):
    h = input()
    for j in range(m):
        if (h[j] == "."):
            used[i][j] = False
            hole[i][j] = False
ansi = []
for i in range(n):
    for j in range(m):
        ans = []
        if (not used[i][j]):
            dfs(i, j)
        if len(ans):
            f = False
            for elem in ans:
                if (not elem[0]) or (not elem[1]) or (elem[0] == n - 1) or (elem[1] == m - 1):
                    f = True
            if not f:
                ansl = [len(ans)] + ans
                ansi.append(ansl)
ansi.sort()
s = 0
for i in range(len(ansi) - k):
    s += ansi[i][0]
    for j in range(1, ansi[i][0] + 1):
        hole[ansi[i][j][0]][ansi[i][j][1]] = True
print(s)
for i in range(n):
    op = ""
    for j in range(m):
        if hole[i][j]:
            op += "*"
        else:
            op += "."
    print(op)
