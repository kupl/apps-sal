from itertools import accumulate
n, h, l, r = map(int, input().split())
a = list(map(int, input().split()))
acc = [0] + list(accumulate(a))
dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
for i in range(1, n + 1):
    for j in range(i + 1):
        x = (acc[i] - j) % h
        if j == 0:
            if l <= x <= r:
                dp[i][j] = dp[i - 1][j] + 1
            else:
                dp[i][j] = dp[i - 1][j]
        else:
            if l <= x <= r:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + 1
            else:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j])
print(max(dp[n]))
