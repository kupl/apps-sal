n, m = map(int, input().split())
a = list(int(input()) for _ in range(m))
dp = [[] for _ in range(n + 1)]
dp[0] = 1
# j = 0
if m == 0:
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
    print(dp[n])
    return
if a[0] == 1:
    dp[1] = 0
    j = 1
else:
    dp[1] = 1
    j = 0
for i in range(2, n + 1):
    # print(i, dp)
    if j < m:
        if a[j] == i:
            dp[i] = 0
            j += 1
            continue
    dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
print(dp[n])
