law = 998244353
n = int(input())
robots = [tuple(map(int, input().split())) for _ in range(n)]

robots.sort(reverse = True)

ntrig = [-1] * n
dp = [0] * n
dp[0] = 2
for i, (x, d) in enumerate(robots):
    if i == 0:
        continue
    next = i-1
    while x + d > robots[next][0]:
        next = ntrig[next]
        if next == -1:
            break
    ntrig[i] = next
    if next == -1:
        dp[i] = dp[i-1] + 1
    else:
        dp[i] = dp[i-1] + dp[next]
    dp[i] %= law

print(dp[n-1])
