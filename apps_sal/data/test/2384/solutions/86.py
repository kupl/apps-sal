import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
m = n // 2
if n % 2 == 0:
    dp = [[-10 ** 18] * 2 for _ in range(m)]
    dp[0][0] = a[0]
    dp[0][1] = a[1]
    for i in range(1, m):
        for j in range(2 * i, 2 * (i + 1)):
            for k in range(2 * (i - 1), 2 * i):
                if j - k > 1:
                    dp[i][j % 2] = max(dp[i][j % 2], dp[i - 1][k % 2] + a[j])
else:
    dp = [[-10 ** 18] * 3 for _ in range(m)]
    dp[0][0] = a[0]
    dp[0][1] = a[1]
    dp[0][2] = a[2]
    for i in range(1, m):
        for j in range(2 * i, 2 * (i + 1) + 1):
            for k in range(2 * (i - 1), 2 * i + 1):
                if j - k > 1:
                    dp[i][j - 2 * i] = max(dp[i][j - 2 * i], dp[i - 1][k - 2 * (i - 1)] + a[j])
print(max(dp[-1]))
