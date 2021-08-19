l = list(map(int, input()))
mod = 10 ** 9 + 7

ln = len(l)
dp = [[0] * 2 for _ in range(2)]
dp[0][1] = 1

for e in l:
    dp_new = [[0] * 2 for _ in range(2)]
    for now in range(2):
        for prev in range(2):
            # same -> same
            if now == e:
                dp_new[now][1] += dp[prev][1] * (now + 1)

            # same -> small
            if now == 0 and e == 1:
                dp_new[now][0] += dp[prev][1]

            # small -> small
            dp_new[now][0] += dp[prev][0] * (now + 1)

    dp = dp_new
    for i in range(2):
        for j in range(2):
            dp[i][j] %= mod

ans = 0
for row in dp:
    ans += sum(row)
    ans %= mod

print(ans)
