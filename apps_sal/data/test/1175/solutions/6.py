MOD = 10**9 + 7

L, R = [int(item) for item in input().split()]
L_blen = L.bit_length()
R_blen = R.bit_length()

dp = [[[0] * (R_blen + 1) for _ in range(2)] for _ in range(2)]

for i in range(R_blen + 1):
    L_bit = L & (1 << R_blen - i)
    R_bit = R & (1 << R_blen - i)

    curbit_idx = R_blen - i + 1
    if curbit_idx <= R_blen and curbit_idx >= L_blen:
        dp[R_blen == curbit_idx][L_blen == curbit_idx][i] += 1

    if not R_bit and not L_bit:
        dp[0][0][i] += dp[0][0][i - 1]
        dp[0][0][i] += dp[0][1][i - 1]
        dp[1][1][i] += dp[1][1][i - 1]
        dp[1][0][i] += dp[1][0][i - 1]
        dp[0][0][i] += dp[0][0][i - 1]
        dp[0][1][i] += dp[0][1][i - 1]
        dp[0][1][i] += dp[0][1][i - 1]
        dp[0][0][i] += dp[0][0][i - 1]

    if R_bit and not L_bit:
        dp[0][0][i] += dp[0][0][i - 1]
        dp[1][0][i] += dp[1][0][i - 1]
        dp[0][0][i] += dp[0][1][i - 1]
        dp[1][0][i] += dp[1][1][i - 1]
        dp[0][0][i] += dp[0][0][i - 1]
        dp[0][0][i] += dp[1][0][i - 1]
        dp[0][1][i] += dp[0][1][i - 1]
        dp[0][1][i] += dp[1][1][i - 1]
        dp[0][0][i] += dp[0][0][i - 1]
        dp[1][0][i] += dp[1][0][i - 1]
        dp[0][1][i] += dp[0][1][i - 1]
        dp[1][1][i] += dp[1][1][i - 1]

    if not R_bit and L_bit:
        dp[0][0][i] += dp[0][0][i - 1]
        dp[0][1][i] += dp[0][1][i - 1]
        dp[0][0][i] += dp[0][0][i - 1]
        dp[1][0][i] += dp[1][0][i - 1]
        dp[0][0][i] += dp[0][0][i - 1]

    if R_bit and L_bit:
        dp[0][0][i] += dp[0][0][i - 1]
        dp[1][0][i] += dp[1][0][i - 1]
        dp[0][1][i] += dp[0][1][i - 1]
        dp[1][1][i] += dp[1][1][i - 1]
        dp[0][0][i] += dp[1][0][i - 1]
        dp[0][0][i] += dp[0][0][i - 1]
        dp[1][0][i] += dp[1][0][i - 1]
        dp[0][0][i] += dp[0][0][i - 1]

    for i in range(2):
        for j in range(2):
            dp[i][j][i] %= MOD

ans = 0
for i in range(2):
    for j in range(2):
        ans += dp[i][j][-1]
        ans %= MOD
print(ans)
