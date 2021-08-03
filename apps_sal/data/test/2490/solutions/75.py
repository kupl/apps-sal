n = input()
dp = [0, 1]
ans = 0
for i in range(len(n)):
    cur1 = dp[0]
    cur2 = dp[1]
    if i != len(n) - 1:
        dp[0] = min(cur1 + int(n[i]), cur2 + 10 - int(n[i]))
        dp[1] = min(cur1 + int(n[i]) + 1, cur2 + 9 - int(n[i]))
    else:
        ans = min(dp[0] + int(n[i]), dp[1] + 10 - int(n[i]))
print(ans)
