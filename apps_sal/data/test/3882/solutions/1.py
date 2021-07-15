mod = 10 ** 9 + 7
n = int(input())
a = [[0] * (n + 1) for i in range(n + 1)]
a[0][0] = 1
for i in range(1, n + 1):
    a[i][0] = a[i - 1][i - 1]
    for j in range(1, i + 1):
        a[i][j] = (a[i][j - 1] + a[i - 1][j - 1]) % mod
print(a[n][n - 1])
