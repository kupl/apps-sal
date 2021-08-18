N = int(input())
P = list(map(int, input().split()))

dp = [0] * N
dp[0] = P[0]
ans = 1
for i in range(1, N):
    if P[i] <= dp[i - 1]:
        dp[i] = P[i]
        ans += 1
    else:
        dp[i] = dp[i - 1]

print(ans)
return
