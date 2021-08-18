import sys

n, m = map(int, input().split())
l1 = [list(input()) for i in range(n)]
l2 = [[0] * m for i in range(n)]
dy = [1, 1, 1, 0, -1, -1, -1, 0]
dx = [-1, 0, 1, 1, 1, 0, -1, -1]
for i in range(n):
    for j in range(m):
        for q in range(8):
            if 0 <= i + dy[q] <= n - 1 and 0 <= j + dx[q] <= m - 1 and l1[i + dy[q]][j + dx[q]] == '*':
                l2[i][j] += 1
for i in range(n):
    for j in range(m):
        if l1[i][j] != '*' and l1[i][j] != '.' and int(l1[i][j]) != l2[i][j]:
            print('NO')
            return
for i in range(n):
    for j in range(m):
        if l1[i][j] == '.' and l2[i][j] != 0:
            print('NO')
            return
print('YES')
