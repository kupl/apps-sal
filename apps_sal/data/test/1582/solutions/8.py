N = int(input())
dp = 100 * [0]
ans = 0

for n in range(N + 1):
    s = str(n)
    dp[10 * int(s[0]) + int(s[-1])] += 1

for i in range(1, 10):
    for j in range(1, 10):
        ans += dp[10 * i + j] * dp[10 * j + i]

print(ans)
