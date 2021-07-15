n = int(input())
l = [[*map(int, input().split())], [*map(int, input().split())]]
dp = [0, 0]
for i in range(n):
    new_dp = dp[:]
    new_dp[0] = max(new_dp[0], dp[1] + l[0][i])
    new_dp[1] = max(new_dp[1], dp[0] + l[1][i])
    dp = new_dp
print(max(dp))
