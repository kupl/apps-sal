import sys
h, w, k = map(int, input().split())

mod = 10 ** 9 + 7

if w == 1:
    print(1)
    return

n_join = [0 for i in range(w - 1)]
n_unjoin = [0 for i in range(w - 1)]
cnt = 0

for i in range(2 ** (w - 1)):
    p = 0
    f = 1
    tmp_join = []
    tmp_unjoin = []
    for j in range(w - 1):
        c = i & (1 << j)
        if c:
            tmp_join.append(j)
        if not (c or p):
            tmp_unjoin.append(j)
        if p and c:
            f = 0
            break
        p = c
    if f:
        cnt += 1
        for j in tmp_join:
            n_join[j] += 1
        for j in tmp_unjoin:
            n_unjoin[j] += 1

n_unjoin.append(cnt - n_join[-1])

dp = [[0 for j in range(w)] for i in range(h)]
dp[0][0] = n_unjoin[0]
dp[0][1] = n_join[0]

for i in range(1, h):
    for j in range(w):
        dp[i][j] += dp[i - 1][j] * n_unjoin[j] % mod
        dp[i][j] %= mod
        if j > 0:
            dp[i][j] += dp[i - 1][j - 1] * n_join[j - 1] % mod
            dp[i][j] %= mod
        if j < w - 1:
            dp[i][j] += dp[i - 1][j + 1] * n_join[j] % mod
            dp[i][j] %= mod

print(dp[h - 1][k - 1])
