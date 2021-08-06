n, m, k = map(int, input().split())
a = [float('-inf')] + list(map(int, input().split()))
if m == 1:
    a.sort()
    print(sum(a[n - k + 1:n + 1]))
    return
s = [0] * (n + 1)
dp = [[0] * (n + 1) for _ in range(k + 1)]
for i in range(1, n + 1):
    s[i] = s[i - 1] + a[i]
for i in range(1, k + 1):
    for j in range(i * m, n + 1):
        dp[i][j] = max(dp[i][j - 1], (s[j] - s[j - m]) + dp[i - 1][j - m])
print(dp[k][n])
