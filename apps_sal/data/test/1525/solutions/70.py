H, W, K = map(int, input().split())

if W == 1:
    print(1 if K == 1 else 0)
    return

MOD = 10 ** 9 + 7

states = [0]
for state in range(1, 1 << (W - 1)):
    flag = True
    for j in range(1, W - 1):
        if ((state >> j - 1) & 1) and ((state >> j) & 1):
            flag = False
    if flag:
        states.append(state)

dp = [[0] * W for _ in range(H + 1)]

dp[0][0] = 1

# 貰うDP
for i in range(H):
    for state in states:
        for j in range(W - 1):
            if (state >> j) & 1:
                dp[i + 1][j] = (dp[i + 1][j] + dp[i][j + 1]) % MOD
                dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j]) % MOD
            else:
                if j == 0:
                    dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % MOD
                elif not ((state >> j - 1) & 1):
                    dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % MOD
                if j == W - 2:
                    dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j + 1]) % MOD

print(dp[H][K - 1])
