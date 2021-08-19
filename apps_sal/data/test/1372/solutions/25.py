(h, n) = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]
dp = [0] * 20001
for i in range(1, h + 1):
    dp[i] = min((dp[i - a] + b for (a, b) in l))
print(dp[h])
