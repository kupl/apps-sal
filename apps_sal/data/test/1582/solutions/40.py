N = int(input())

dp = [[0] * 9 for _ in range(9)]

for i in range(1, N + 1):
    if i % 10:
        st = str(i)
        start = int(st[0])
        end = int(st[-1])
        dp[start - 1][end - 1] += 1

ans = 0

for i in range(9):
    for j in range(9):
        ans += dp[i][j] * dp[j][i]

print(ans)
