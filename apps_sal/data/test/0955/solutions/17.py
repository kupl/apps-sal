N = int(input())
src = [input().split() for i in range(N)]
INF = float('inf')
dp = [INF] * 8
dp[0] = 0
for (n, vs) in src:
    n = int(n)
    b = int('A' in vs) * 4
    b += int('B' in vs) * 2
    b += int('C' in vs) * 1
    dp2 = dp[:]
    for (i, c) in enumerate(dp):
        dp2[i | b] = min(dp2[i | b], c + n)
    dp = dp2
print(-1 if dp[-1] == INF else dp[-1])
