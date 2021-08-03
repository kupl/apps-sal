n = int(input())
l = list(map(int, input().split()))
m = n // 2
t = n % 2 + 2
dp = [0] * t
for i in range(m):
    for j in range(t):
        dp[j] += l[2 * i + j]
    for j in range(1, t):
        dp[j] = max(dp[j], dp[j - 1])
print(dp[-1])
