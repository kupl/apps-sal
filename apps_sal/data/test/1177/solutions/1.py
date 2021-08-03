n, s = list(map(int, input().split()))
arr = list(map(int, input().split()))

mod = 998244353
dp = [0] * (s + 1)
ans = 0

for i in range(n):
    dp[0] += 1
    tmp = arr[i]
    for j in range(s, tmp - 1, -1):
        dp[j] += dp[j - tmp]
    ans += dp[s]
    ans %= mod

print(ans)
