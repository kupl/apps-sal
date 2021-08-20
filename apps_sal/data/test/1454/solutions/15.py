(n, m) = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
res = 0
for i in range(n - 2, 0, -1):
    for j in range(m - 1, 0, -1):
        if matrix[i][j] == 0:
            mn = min(matrix[i + 1][j], matrix[i][j + 1])
            if mn != 1:
                matrix[i][j] = mn - 1
            else:
                res = -1
                break
    if res == -1:
        break
else:
    for i in range(n):
        if [matrix[i][j] for j in range(m - 1) if matrix[i][j] >= matrix[i][j + 1]]:
            res = -1
            break
    else:
        for j in range(m):
            if [matrix[i][j] for i in range(n - 1) if matrix[i][j] >= matrix[i + 1][j]]:
                res = -1
                break
        else:
            res = sum((sum(matrix[i]) for i in range(n)))
print(res)
