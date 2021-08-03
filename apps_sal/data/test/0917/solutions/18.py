n, h, m = list(map(int, input().split()))
dp = [h for _ in range(n)]
for _ in range(m):
    l, r, x = list(map(int, input().split()))
    for i in range(l - 1, r):
        dp[i] = min(dp[i], x)
ans = 0
for x in dp:
    ans += x * x
print(ans)
