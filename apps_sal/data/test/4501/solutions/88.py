(N, A) = (int(T) for T in input().split())
X = [int(T) - A for T in input().split()]
DP = [[0] * (2 * (50 * N) + 1) for TI in range(0, N + 1)]
DP[0][50 * N] = 1
for TI in range(0, N):
    for TS in range(0, 2 * 50 * N + 1):
        if DP[TI][TS] != 0:
            DP[TI + 1][TS] += DP[TI][TS]
            DP[TI + 1][TS + X[TI]] += DP[TI][TS]
print(DP[N][50 * N] - 1)
