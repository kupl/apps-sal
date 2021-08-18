import collections


n, a, b = list(map(int, input().split()))

s = " " + input()

maxn = n + 1

dp = [0x3f for _ in range(maxn)]
v = [[0 for _c in range(maxn)] for _r in range(maxn)]
Next = [0 for _n in range(maxn)]

for i in range(1, n + 1):
    for j in range(i, n + 1):
        if s[i] == s[j]:
            v[i][j] = v[i - 1][j - 1] + 1

dp[0] = 0
for i in range(1, n + 1):
    dp[i] = dp[i - 1] + a
    for j in range(1, i):
        t = min(i - j, v[j][i])
        if t:
            dp[i] = min(dp[i], dp[i - t] + b)

print(dp[n])
