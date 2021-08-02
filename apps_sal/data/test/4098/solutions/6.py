n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
l = r = 0
b = [0] * n
for _ in range(n):
    while l < r and a[r] - a[l] > 5:
        l += 1
    b[r] = l
    r += 1
dp = [[0 for _ in range(k + 1)] for _ in range(n)]
for i in range(1, k + 1):
    dp[0][i] = 1
for i in range(1, n):
    for j in range(1, k + 1):
        dp[i][j] = max(dp[i - 1][j], (dp[b[i] - 1][j - 1] if b[i] >= 1 else 0) + (i - b[i] + 1))
print(dp[-1][-1])
