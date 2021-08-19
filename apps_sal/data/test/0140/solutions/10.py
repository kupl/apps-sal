(n, m) = list(map(int, input().split()))
a = []
for i in range(n):
    (b, c) = list(map(int, input().split()))
    a.append((max(0, b - c), min(b + c, m)))
dp = [0] * (m + 1)
for i in range(1, m + 1):
    dp[i] = i
    for j in range(n):
        (c, d) = a[j]
        if c <= i and i <= d:
            dp[i] = dp[i - 1]
        elif i < c:
            cost = c - i
            dp[i] = min(dp[i], cost + dp[max(0, c - cost - 1)])
        elif i > d:
            cost = i - d
            dp[i] = min(dp[i], cost + dp[max(0, c - cost - 1)])
print(dp[m])
