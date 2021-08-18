n, m, k = list(map(int, input().split()))
p = [0] + list(map(int, input().split()))
if m == 1:
    print(sum(sorted(p)[-k:]))
    return
pref = [0]
for i in range(1, n + 1):
    pref += [pref[i - 1] + p[i]]
dp = [[0] * (k + 1) for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, k + 1):
        if j * m > i:
            dp[i][j] = 0
        if i - m >= 0:
            dp[i][j] = max(dp[i - 1][j], dp[i - m][j - 1] + pref[i] - pref[i - m])
        else:
            dp[i][j] = dp[i - 1][j]
print(dp[n][k])
