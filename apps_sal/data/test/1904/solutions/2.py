n = int(input())
s = list(input())
a = list(map(int, input().split()))
dp = [1e+20 for _ in range(4)]
dp[0] = 0
for i in range(n):
    if s[i] == 'h':
        dp[1] = min(dp[0], dp[1])
        dp[0] += a[i]
    elif s[i] == 'a':
        dp[2] = min(dp[1], dp[2])
        dp[1] += a[i]
    elif s[i] == 'r':
        dp[3] = min(dp[2], dp[3])
        dp[2] += a[i]
    elif s[i] == 'd':
        dp[3] += a[i]
ans = min(dp)
print(ans)
