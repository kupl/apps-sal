import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
A = []

for i in range(n):
    A.append(input() + '1')

A.append('1' * (m + 1))
ans = 0
used = [[False] * m for i in range(n)]
B = ''.join(A)
B = list(set(B))
def dfs(i, j, b, c):
    nonlocal ans
    used[i][j] = True
    
    if A[i - 1][j] == b and c != 3:
        if used[i - 1][j]:
            ans = 1
        else:
            dfs(i - 1, j, b, 1)

    if A[i][j + 1] == b and c != 4:
        if used[i][j + 1]:
            ans = 1
        else:
            dfs(i, j + 1, b, 2)

    if A[i + 1][j] == b and c != 1:
        if used[i + 1][j]:
            ans = 1
        else:
            dfs(i + 1, j, b, 3)

    if A[i][j - 1] == b and c != 2:
        if used[i][j - 1]:
            ans = 1
        else:
            dfs(i, j - 1, b, 4)

for i in range(len(B)):
    used = [[False] * m for i in range(n)]
    if B[i] != '1':
        b = B[i]
        for x in range(n):
            for y in range(m):
                if A[x][y] == b and not used[x][y]:
                    dfs(x, y, b, -1)

if ans == 0:
    print('No')
else:
    print('Yes')
