n, k, m = list(map(int, input().split()))
s = [int(x) for x in input().split()]
S = sorted(s)
S = S[::-1]
dp = [S[0]]
for i in range(1, len(s)):
    dp.append(dp[-1] + S[i])
dp = dp[::-1]
br = len(dp)
for i in range(0, len(dp)):
    if(i <= m):
        dp[i] = dp[i] + min(m - i, (n - i) * k)
    else:
        br = i
        break
dp = dp[:br]


ans = -1
for i in range(0, len(dp)):
    ans = max(ans, dp[i] / (n - i))
print(ans)
