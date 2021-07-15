n, m = map(int, input().split())
a = [int(input()) for _ in range(m)]

mod = 10**9 + 7
c = [0]*(n+1)
for i in a:
    c[i] = -1
dp = [0]*(n+1)
dp[0] = 1
dp[1] = 0 if m > 0 and a[0] == 1 else 1
for i in range(2, n+1):
    if c[i] == -1:
        continue
    dp[i] = (dp[i-1] + dp[i-2]) % mod
print(dp[-1])
