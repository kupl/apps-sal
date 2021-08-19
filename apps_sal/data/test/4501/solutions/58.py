(n, a) = map(int, input().split())
x = list(map(int, input().split()))
t = [[[0] * (50 * (j + 1) + 1) for j in range(i + 2)] for i in range(n + 1)]
ans = 0
t[0][0][0] = 1
for i in range(1, n + 1):
    for j in range(i + 1):
        for k in range(50 * j + 1):
            if j >= 1 and k >= x[i - 1]:
                t[i][j][k] = t[i - 1][j - 1][k - x[i - 1]] + t[i - 1][j][k]
            else:
                t[i][j][k] = t[i - 1][j][k]
for i in range(1, n + 1):
    ans += t[n][i][i * a]
print(ans)
