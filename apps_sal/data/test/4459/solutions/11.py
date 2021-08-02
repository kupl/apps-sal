n = int(input())
a = [int(i) for i in input().split()]

dp = [0] * (n + 2)
for i in a:
    if i > n:
        dp[-1] += 1
    else:
        dp[i] += 1

ans = dp[-1]
for i in range(1, n + 1):
    if dp[i] >= i:
        ans += dp[i] - i
    else:
        ans += dp[i]
print(ans)
