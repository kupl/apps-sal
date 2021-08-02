n, m = map(int, input().split())
a = [int(input()) for _ in range(m)]

mod = 10**9 + 7
a.append(float('INF'))
a = a[::-1]
dp = [0] * (n + 1)
dp[0] = 1
if a[-1] != 1:
    dp[1] = 1
else:
    a.pop()
for i in range(2, n + 1):
    if i == a[-1]:
        a.pop()
        continue
    dp[i] = dp[i - 1] + dp[i - 2]
    dp[i] %= mod
print(dp[n])
