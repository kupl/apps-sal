(n, k) = map(int, input().split())
s = input()
dp = [[0] * 102 for i in range(102)]
dp1 = [[0] * 102 for i in range(30)]
for i in range(0, n + 1):
    dp[i][0] = 1
for i in range(1, n + 1):
    nm = ord(s[i - 1]) - ord('a')
    for le in range(1, i + 1):
        dp[i][le] = dp[i - 1][le] + dp[i - 1][le - 1]
        dp[i][le] -= dp1[nm][le]
    for le in range(1, i + 1):
        dp1[nm][le] += dp[i][le] - dp[i - 1][le]
ans = 0
for le in range(n, -1, -1):
    if k == 0:
        break
    x = min(dp[n][le], k)
    ans += (n - le) * x
    k -= x
if k != 0:
    print(-1)
else:
    print(ans)
