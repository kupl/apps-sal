(n, m) = [int(x) for x in input().split()]
M = [[1 if k == 'B' else -1 for k in input()] for i in range(n)]
P = [[0 for j in range(m + 1)] for i in range(n + 1)]
for i in range(n):
    for j in range(m):
        P[i][j] += M[i][j]
        P[i + 1][j + 1] += M[i][j]
        P[i + 1][j] -= M[i][j]
        P[i][j + 1] -= M[i][j]
print(n * m - sum((P[i][1:].count(0) for i in range(1, n + 1))))
