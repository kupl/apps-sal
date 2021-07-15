n, c = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dp = [[0, 0] for i in range(n)]
dp[0] = [0, c]
for i in range(1, n):
    ans1 = dp[i - 1][0] + a[i - 1]
    ans2 = dp[i - 1][1] + b[i - 1]
    dp[i][1] = min(ans2, dp[i - 1][0] + c + b[i - 1])
    dp[i][0] = min(ans1, dp[i][1])
for elem in dp:
    print(min(elem[0], elem[1]), end=" ")
