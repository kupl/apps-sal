h, w, k = map(int, input().split())
dp = [[0 for _ in range(w)]for _ in range(h + 1)]
dp[0][0] = 1
mod = 10**9 + 7
for i in range(h):
    for bit in range(2**(w - 1)):
        bit = bin(bit)[2:].zfill(w - 1)
        f = 0
        for j in range(w - 2):
            if bit[j] == '1' and bit[j + 1] == '1':
                f = 1
                break
        if f:
            continue
        for j in range(w):
            if j == 0:
                dp[i + 1][j] += dp[i][j + 1] if bit[0] == '1' else dp[i][j]
            elif j == w - 1:
                dp[i + 1][j] += dp[i][j - 1] if bit[-1] == '1' else dp[i][j]
            else:
                dp[i + 1][j] += dp[i][j] * (bit[j - 1] == '0' and bit[j] == '0')
                dp[i + 1][j] += dp[i][j - 1] * (bit[j - 1] == '1')
                dp[i + 1][j] += dp[i][j + 1] * (bit[j] == '1')
            dp[i + 1][j] %= mod
print(dp[-1][k - 1])
