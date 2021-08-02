l = list(map(int, input()))
mod = 10 ** 9 + 7

ln = len(l)
dp = [0] * 2
dp[1] = 1

for e in l:
    dp_new = [0] * 2
    # exact -> exact
    dp_new[1] += dp[1] * (e + 1)

    # exact -> small
    if e == 1:
        dp_new[0] += dp[1]

    # small -> small
    dp_new[0] += dp[0] * 3

    dp = dp_new
    for i in range(2):
        dp[i] %= mod

ans = sum(dp) % mod

print(ans)
