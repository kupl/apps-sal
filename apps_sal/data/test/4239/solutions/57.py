n = int(input())

dp = [0]
# dp[n]を求める

for i in range(1, n + 1):
    c = []
    c.append(dp[i - 1] + 1)
    p6 = 1
    while i >= 6**p6:
        c.append(dp[i - 6**p6] + 1)
        p6 += 1

    p9 = 1
    while i >= 9**p9:
        c.append(dp[i - 9**p9] + 1)
        p9 += 1

    dp.append(min(c))

print(dp[n])
