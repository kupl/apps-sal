import sys
readline = sys.stdin.readline
N = int(readline())
INF = 10 ** 10
dp = [INF] * (N + 1)
dp[0] = 0
for i in range(10, 0, -1):
    for j in range(N + 1):
        if dp[j] != INF:
            if j + 6 ** i <= N:
                dp[j + 6 ** i] = min(dp[j + 6 ** i], dp[j] + 1)
            if j + 9 ** i <= N:
                dp[j + 9 ** i] = min(dp[j + 9 ** i], dp[j] + 1)
ans = INF
for i in range(len(dp) - 1, -1, -1):
    money = dp[i] + N - i
    if ans > money:
        ans = money
print(ans)
