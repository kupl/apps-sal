n = int(input())

dp = {1: 2, 2: 3}


def cost(i):
    if i not in dp:
        dp[i] = cost(i - 1) + cost(i - 2)
    return dp[i]


ans = 1

while cost(ans) <= n:
    ans += 1

print(ans - 1)
