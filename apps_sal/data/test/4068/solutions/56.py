n, m = list(map(int, input().split()))
a = list(int(input()) for _ in range(m))

MOD = 10**9 + 7
is_broken = [0] * (n + 1)
dp = [0] * (n + 1)
dp[0] = 1

for x in a:
    is_broken[x] = 1

for i in range(n):
    for j in range(i + 1, min(n, i + 2) + 1):
        if not is_broken[j]:
            dp[j] += dp[i]
            dp[j] %= MOD

print((dp[n]))
