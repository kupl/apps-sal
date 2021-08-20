(N, M) = map(int, input().split())
dp = [0] * (N + 1)
for i in range(M):
    (l, r) = map(int, input().split())
    dp[l - 1] += 1
    dp[r] -= 1
for i in range(N):
    dp[i + 1] += dp[i]
ans = 0
for i in range(N):
    if dp[i] == M:
        ans += 1
print(ans)
