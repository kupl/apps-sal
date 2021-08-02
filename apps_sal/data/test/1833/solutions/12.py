n = int(input())
a = list(map(int, input().split()))
dp = [0] * (1000001)
dp[0] = 1
for i in range(n):
    x = int(a[i]**.5)
    for j in range(min(i + 1, x), 0, -1):
        if a[i] % j == 0:
            if a[i] / j > x and a[i] / j <= n:
                dp[a[i] // j] += dp[a[i] // j - 1]
            dp[j] += dp[j - 1]
ans = 0
for i in range(1, n + 1):
    ans += dp[i]
    ans %= 1000000007
print(ans)
