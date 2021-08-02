N, K = map(int, input().split())
move = set()
MOD = 998244353
move = []
for i in range(K):
    move.append(tuple(map(int, input().split())))


dp = [0] * (2 * N + 3)
add = [0] * (2 * N + 3)
height = 0
dp[0] = dp[1] = 1
for i in range(1, N + 1):
    height += add[i] % MOD
    if i != 1:
        dp[i] = height
    for L, R in move:
        add[i + L] += dp[i] % MOD
        add[i + R + 1] -= dp[i] % MOD
print(dp[N] % MOD)
