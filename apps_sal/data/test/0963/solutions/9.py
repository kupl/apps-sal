n, k = map(int, input().split())
mod = 998244353
s = []

for i in range(k):
    si = list(map(int, input().split()))
    s.append(si)

dp = [0] * (n + 1)
dpsum = [0] * (n + 1)
dp[1] = 1
dpsum[1] = 1

for j in range(2, n + 1):
    for m in range(k):
        l = j - s[m][0]
        r = j - s[m][1]
        if l < 0:
            continue
        r = max(r, 1)
        dp[j] += dpsum[l] - dpsum[r - 1]
    dpsum[j] = (dpsum[j - 1] + dp[j]) % mod

ans = dp[n] % mod
print(ans)
