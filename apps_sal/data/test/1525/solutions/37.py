def is_valid(k):
    n = k.bit_length()

    for i in range(n - 1):
        if (k >> i) & 1 and (k >> i + 1) & 1:
            return False

    return True


p = 10**9 + 7

H, W, K = map(int, input().split())

dp = [[0] * W for _ in range(H + 1)]

dp[0][0] = 1

for i in range(H):
    for j in range(1 << (W - 1)):
        if not is_valid(j):
            continue
        for k in range(W):
            if k < W - 1 and (j >> k) & 1:
                dp[i + 1][k + 1] += dp[i][k]
                dp[i + 1][k + 1] %= p
            elif k > 0 and (j >> (k - 1)) & 1:
                dp[i + 1][k - 1] += dp[i][k]
                dp[i + 1][k - 1] %= p
            else:
                dp[i + 1][k] += dp[i][k]
                dp[i + 1][k] %= p

print(dp[H][K - 1] % p)
