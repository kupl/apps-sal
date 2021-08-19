MOD = 10 ** 9 + 7

n = int(input())
# (used ?) * 3 + cur
dp = [0] * 12
qcnt = 0
for c in input():
    new_dp = dp.copy()
    if c == 'a':
        new_dp[0] += 1
        new_dp[0] %= MOD
    elif c == 'b':
        new_dp[1] += dp[0]
        new_dp[1] %= MOD
        new_dp[4] += dp[3]
        new_dp[4] %= MOD
        new_dp[7] += dp[6]
        new_dp[7] %= MOD
        new_dp[10] += dp[9]
        new_dp[10] %= MOD
    elif c == 'c':
        new_dp[2] += dp[1]
        new_dp[2] %= MOD
        new_dp[5] += dp[4]
        new_dp[5] %= MOD
        new_dp[8] += dp[7]
        new_dp[8] %= MOD
        new_dp[11] += dp[10]
        new_dp[11] %= MOD
    else:
        qcnt += 1
        new_dp[3] += 1
        for i in range(8):
            if i % 3 == 2:
                continue
            new_dp[i + 4] += dp[i]
            new_dp[i] %= MOD
    dp = new_dp
    # print(dp)

ans = 0
for i in range(4):
    if qcnt - i < 0:
        break
    tmp = pow(3, qcnt - i, MOD)
    tmp *= dp[2 + 3 * i]
    ans += tmp % MOD
    ans %= MOD
# print(dp[2::3])
print(ans)
