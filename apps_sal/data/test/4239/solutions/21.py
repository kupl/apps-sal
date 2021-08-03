N = int(input())
inf = 100000
dp = [inf for _ in range(N + 1)]
dp[0] = 0
for n in range(1, N + 1):
    num = 100000
    i = 0
    j = 0
    while 9**(i + 1) <= n:
        i += 1
    while 6**(j + 1) <= n:
        j += 1
    for k in range(i + 1):
        num = min(num, dp[n - 9**k] + 1)
    for k in range(j + 1):
        num = min(num, dp[n - 6**k] + 1)
    dp[n] = min(dp[n], num)
print(dp[N])
