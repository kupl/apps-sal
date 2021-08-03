

n = int(input())
a = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1] for i in range(10)]
for i in range(1, n):
    for j in range(1, n):
        a[i][j] = a[i - 1][j] + a[i][j - 1]
print(a[n - 1][n - 1])
