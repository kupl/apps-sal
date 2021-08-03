n, m = map(int, input().split())
dp = [0] * (2**n + 1)
for i in range(m):
    a, b = map(int, input().split())
    c = list(map(int, input().split()))
    temp = 0
    for i in c:
        temp += 2 ** (i - 1)
    for i in range(2**n):
        if i != 0 and dp[i] == 0:
            continue
        t = i | temp
        if dp[t] == 0:
            dp[t] = dp[i] + a
        else:
            dp[t] = min(dp[i] + a, dp[t])

ans = dp[2**n - 1]
if ans == 0:
    print(-1)
else:
    print(ans)
