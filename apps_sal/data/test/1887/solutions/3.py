from sys import stdin, stdout, exit

n = int(stdin.readline())
top = list(map(int, stdin.readline().split()))
bot = list(map(int, stdin.readline().split()))

top_dp = [0]*(n+1)
bot_dp = [0]*(n+1)

for i in range(n):
    top_dp[i+1] = max(top_dp[i], bot_dp[i] + top[i])
    bot_dp[i+1] = max(bot_dp[i], top_dp[i] + bot[i])

ans = max(top_dp[n], bot_dp[n])
stdout.write(str(ans) + "\n")

