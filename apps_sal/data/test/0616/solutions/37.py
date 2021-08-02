n, m = list(map(int, input().split()))
g = (1 << n)

dp = [float("inf")] * g
dp[0] = 0
for i in range(m):
    a, b = list(map(int, input().split()))
    c_l = list(map(int, input().split()))
    f = 0
    for c_i in c_l:
        f += 1 << (c_i - 1)
    for j in range(g - 1, -1, -1):
        dp[j | f] = min(dp[j] + a, dp[j | f])

print((-1 if dp[-1] == float("inf") else dp[-1]))
