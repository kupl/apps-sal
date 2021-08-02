n, m = map(int, input().split())
s = list(map(int, input().split()))
t = list(map(int, input().split()))
mod = 10**9 + 7
dp = [1] * (m + 1)
for i in range(n):
    ndp = [0] * (m + 1)
    ndp[0] = 1
    for j in range(m):
        if s[i] == t[j]:
            ndp[j + 1] = (ndp[j] + dp[j + 1]) % mod
        else:
            ndp[j + 1] = (ndp[j] + dp[j + 1] - dp[j]) % mod
    dp = ndp
print(dp[-1])
