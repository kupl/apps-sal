(n, m) = list(map(int, input().split()))
s = [0] + list(map(int, input().split()))
dp = [[[False for i in range(m + 1)] for j in range(m + 1)] for k in range(2)]
dp[0][0][0] = True
cur = 0
for i in range(1, n + 1):
    cur += 1
    cur %= 2
    last = (cur + 1) % 2
    for j in range(m + 1):
        for k in range(j + 1):
            if j - s[i] > -1 and k - s[i] > -1:
                dp[cur][j][k] = dp[last][j][k] or dp[last][j - s[i]][k] or dp[last][j - s[i]][k - s[i]]
            elif j - s[i] > -1:
                dp[cur][j][k] = dp[last][j][k] or dp[last][j - s[i]][k]
            elif k - s[i] > -1:
                dp[cur][j][k] = dp[last][j][k] or dp[last][j - s[i]][k - s[i]]
            else:
                dp[cur][j][k] = dp[last][j][k]
ans = []
for i in range(k + 1):
    if dp[cur][k][i]:
        ans.append(i)
print(len(ans))
print(*ans)
