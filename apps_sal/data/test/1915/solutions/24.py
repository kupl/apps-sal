n = int(input())
a = [[1] * n for i in range(n)]
for i in range(1, n):
    for j in range(1, n):
        a[i][j] = a[i - 1][j] + a[i][j - 1]
ans = 1
for i in range(1, n):
    for j in range(1, n):
        ans = max(ans, a[i][j])
print(ans)
