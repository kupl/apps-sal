(n, m, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
best = 0
dp = [0] * (n + 1)
for i in range(n):
    b2 = 0
    for j in range(max(-1, i - m), i + 1):
        b2 = max(b2, dp[j] - k + sum(a[j + 1:i + 1]))
    dp[i] = max(b2, a[i] - k)
    best = max(best, dp[i])
print(best)
