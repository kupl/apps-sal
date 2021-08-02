n = int(input())
t = [[0] * n for i in range(n)]
for i in range(n):
    t[0][i] = 1
    t[i][0] = 1
for i in range(1, n):
    for j in range(1, n):
        t[i][j] = t[i - 1][j] + t[i][j - 1]
print(t[n - 1][n - 1])
