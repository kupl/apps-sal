MOD = 10 ** 9 + 7
N = int(input())
K = len(bin(N)) - 2
DP = [[0] * 3 for _ in range(K + 1)]
DP[0][0] = 1
for k in range(K):
    if N & 1 << K - k - 1:
        DP[k + 1][0] = DP[k][0]
        DP[k + 1][1] = (DP[k][0] + DP[k][1]) % MOD
        DP[k + 1][2] = (DP[k][1] * 2 + DP[k][2] * 3) % MOD
    else:
        DP[k + 1][0] = (DP[k][0] + DP[k][1]) % MOD
        DP[k + 1][1] = DP[k][1]
        DP[k + 1][2] = (DP[k][1] + DP[k][2] * 3) % MOD
print(sum(DP[-1]) % MOD)
