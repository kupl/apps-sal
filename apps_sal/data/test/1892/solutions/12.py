MOD = int(1000000000.0 + 7)
n = int(input())
a = []
for i in range(n):
    a.append(input())
a = ''.join(a)
(dp, s) = ([], [])
for i in range(n + 1):
    dp.append([0] * (n + 1))
    s.append([0] * (n + 1))
dp[0][0] = 1
s[0][0] = 1
for i in range(1, n):
    for j in range(0, n):
        if a[i - 1] == 'f':
            dp[i][j + 1] = dp[i - 1][j] % MOD
        elif a[i - 1] == 's':
            dp[i][j] = s[i - 1][j] % MOD
    for j in reversed(list(range(n))):
        s[i][j] += (dp[i][j] + s[i][j + 1]) % MOD
print(s[n - 1][0] % MOD)
