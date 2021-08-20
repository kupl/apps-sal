n = int(input())
dp = [100000] * (n + 1)
dp[0] = 0
for i in range(1, n + 1):
    for j in range(1, 7):
        ind = i - 6 ** j
        if ind >= 0:
            dp[i] = min(dp[i], dp[ind] + 1)
        else:
            break
    for j in range(1, 6):
        ind = i - 9 ** j
        if ind >= 0:
            dp[i] = min(dp[i], dp[ind] + 1)
        else:
            break
    dp[i] = min(dp[i], dp[i - 1] + 1)
print(dp[n])
