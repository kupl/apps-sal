dp = []
for i in range(5005):
    dp.append([0] * 5005)

n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
p = [0] * (n + 1)
for i in range(n):
    z = a[i] - 5
    for j in range(i + 1):
        if a[j] >= z:
            p[i] = j
            break
ans = -1
for i in range(1, n + 1):
    for j in range(k + 1):
        dp[i][j] = max(dp[i - 1][j], dp[p[i - 1]][j - 1] + (i - p[i - 1]))
        if j != k:
            ans = max(ans, dp[i][j])
print(ans)
