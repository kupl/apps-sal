n, m = map(int, input().split())

dp = [10**9] * (1 << n)
dp[0] = 0
for _ in range(m):
    a, b = map(int, input().split())
    key = 0
    for i in map(int, input().split()):
        key += 1 << (i - 1)
    for i in range(1 << n):
        dp[i | key] = min(dp[i | key], dp[i] + a)
if dp[-1] > 10**8:
    print(-1)
else:
    print(dp[-1])
