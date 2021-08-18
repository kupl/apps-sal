n, kk = list(map(int, input().split()))
s = '@' + input()
dp = [[0] * (n + 1) for i in range(n + 1)]
dp[0][0] = 1
for i in range(1, n + 1):
    for j in range(i, n + 1):
        tag = [True] * 26
        for k in range(j, n + 1):
            idx = ord(s[k]) - ord('a')
            if tag[idx]:
                dp[i][k] += dp[i - 1][j - 1]
                tag[idx] = False
ans = 0
for i in range(n, -1, -1):
    tmp = sum(dp[i])
    if kk > tmp:
        kk -= tmp
        ans += (n - i) * tmp
    else:
        ans += kk * (n - i)
        kk = 0
        break
if kk > 0:
    ans = -1
print(ans)
