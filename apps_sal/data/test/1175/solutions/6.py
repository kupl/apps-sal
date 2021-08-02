MOD = 10**9 + 7

L, R = [int(item) for item in input().split()]
L_blen = L.bit_length()
R_blen = R.bit_length()

# dp[y loose/tight][x loose/tight][index]
dp = [[[0] * (R_blen + 1) for _ in range(2)] for _ in range(2)]

for i in range(R_blen + 1):
    L_bit = L & (1 << R_blen - i)
    R_bit = R & (1 << R_blen - i)

    # Form R's MSB to L's LSB can be the initial bit
    curbit_idx = R_blen - i + 1
    if curbit_idx <= R_blen and curbit_idx >= L_blen:
        dp[R_blen == curbit_idx][L_blen == curbit_idx][i] += 1

    # R=0, L=0
    if not R_bit and not L_bit:
        # y=1, x=1
        dp[0][0][i] += dp[0][0][i - 1]
        dp[0][0][i] += dp[0][1][i - 1]
        # y=0, x=0
        dp[1][1][i] += dp[1][1][i - 1]
        dp[1][0][i] += dp[1][0][i - 1]
        dp[0][0][i] += dp[0][0][i - 1]
        dp[0][1][i] += dp[0][1][i - 1]
        # y=1, x=0
        dp[0][1][i] += dp[0][1][i - 1]
        dp[0][0][i] += dp[0][0][i - 1]

    # R=1, L=0
    if R_bit and not L_bit:
        # y=1, x=1
        dp[0][0][i] += dp[0][0][i - 1]
        dp[1][0][i] += dp[1][0][i - 1]
        dp[0][0][i] += dp[0][1][i - 1]
        dp[1][0][i] += dp[1][1][i - 1]
        # y=0, x=0
        dp[0][0][i] += dp[0][0][i - 1]
        dp[0][0][i] += dp[1][0][i - 1]
        dp[0][1][i] += dp[0][1][i - 1]
        dp[0][1][i] += dp[1][1][i - 1]
        # y=1, x=0
        dp[0][0][i] += dp[0][0][i - 1]
        dp[1][0][i] += dp[1][0][i - 1]
        dp[0][1][i] += dp[0][1][i - 1]
        dp[1][1][i] += dp[1][1][i - 1]

    # R=0, L=1
    if not R_bit and L_bit:
        # y=1, x=1
        dp[0][0][i] += dp[0][0][i - 1]
        dp[0][1][i] += dp[0][1][i - 1]
        # y=0, x=0
        dp[0][0][i] += dp[0][0][i - 1]
        dp[1][0][i] += dp[1][0][i - 1]
        # y=1, x=0
        dp[0][0][i] += dp[0][0][i - 1]

    # R=1, L=1
    if R_bit and L_bit:
        # y=1, x=1
        dp[0][0][i] += dp[0][0][i - 1]
        dp[1][0][i] += dp[1][0][i - 1]
        dp[0][1][i] += dp[0][1][i - 1]
        dp[1][1][i] += dp[1][1][i - 1]
        # y=0, x=0
        dp[0][0][i] += dp[1][0][i - 1]
        dp[0][0][i] += dp[0][0][i - 1]
        # y=1, x=0
        dp[1][0][i] += dp[1][0][i - 1]
        dp[0][0][i] += dp[0][0][i - 1]

    # Take MOD
    for i in range(2):
        for j in range(2):
            dp[i][j][i] %= MOD

ans = 0
for i in range(2):
    for j in range(2):
        ans += dp[i][j][-1]
        ans %= MOD
print(ans)
