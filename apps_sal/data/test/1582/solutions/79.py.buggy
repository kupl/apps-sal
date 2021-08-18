n = int(input())
if n <= 9:
    print(n)
    return
dp = [[0] * 10 for _ in range(10)]
for k in range(1, n + 1):
    s = str(k)
    dp[int(s[0])][int(s[-1])] += 1
ans = 0
for i in range(10):
    for j in range(10):
        ans += dp[i][j] * dp[j][i]
print(ans)
