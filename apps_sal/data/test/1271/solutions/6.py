INF = 100000

n, s, k = list(map(int, input().split()))
r = list(map(int, input().split()))
c = input().rstrip()
# dp[i][j]: i = the current position just after eating candies, j = remaining candies to eat
dp = [[INF for j in range(k + 1)] for i in range(n)]
s -= 1
for i in range(n):
    dp[i][k - r[i]] = abs(s - i)
for j in range(k, -1, -1):
    for i in range(n):
        if dp[i][j] >= INF:
            continue
        for f in range(n):
            if r[f] <= r[i]:
                continue
            if c[f] == c[i]:
                continue
            new_val = max(0, j - r[f])
            dp[f][new_val] = min(dp[f][new_val], dp[i][j] + abs(i - f))
ans = INF
for i in range(n):
    ans = min(ans, dp[i][0])
if ans >= INF:
    ans = -1

print(ans)
