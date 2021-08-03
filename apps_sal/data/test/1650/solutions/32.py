l = list(map(int, input()))
mod = 10 ** 9 + 7

ln = len(l)
dp = [[0] * 2 for _ in range(2)]
dp[0][1] = 1

for e in l:
    dp_new = [[0] * 2 for _ in range(2)]
    for i in range(2):
        # same -> same
        if i == e:
            dp_new[i][1] += (dp[0][1] + dp[1][1]) * (1 + i)

        # same -> small
        if i == 0 and e == 1:
            dp_new[0][0] += dp[0][1] + dp[1][1]

        # small -> small
        dp_new[i][0] += (dp[0][0] + dp[1][0]) * (1 + i)

    dp = dp_new
    for i in range(2):
        for j in range(2):
            dp[i][j] %= mod

ans = 0
for row in dp:
    ans += sum(row)
    ans %= mod

print(ans)
