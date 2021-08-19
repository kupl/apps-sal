ans = 0
n, m = map(int, input().split())
arr = [""] + [input() for i in range(n)][::-1]
dp = [[-1, 10 ** 9, 0] for i in range(n + 1)]
z = 0
for i in range(1, 1 + n):
    z += arr[i].count("1")
for i in range(1, n + 1):
    l = arr[i].find("1")
    r = arr[i].rfind("1")
    z -= arr[i].count("1")
    if l != -1:
        dp[i][0] = min(dp[i - 1][0] + 2 * r, dp[i - 1][1] + m + 1) + 1
        dp[i][1] = min(dp[i - 1][0] + m + 1, dp[i - 1][1] + 2 * (m + 1 - l)) + 1
        dp[i][2] = min(dp[i - 1][0] + r, dp[i - 1][1] + (m + 1 - l)) + 1
    else:
        dp[i][0] = min(dp[i - 1][0], dp[i - 1][1] + m + 1) + 1
        dp[i][1] = min(dp[i - 1][0] + m + 1, dp[i - 1][1]) + 1

    #print(dp[i], l, r, arr[i][l], arr[i])
    #print(z, i)
    if z == 0:
        ans = dp[i][2]
        break
print(ans)
