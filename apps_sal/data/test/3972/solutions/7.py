N = int(input())
mod = 10**9 + 7
DP = [0] * (N * 2 + 5)
X = [0] * (N * 2 + 5)
Y = [0] * (N * 2 + 5)
C = 0
Y[0] = -1
for i in range(N):
    C = (C + X[i]) % mod
    DP[i] = (C - Y[i]) % mod
    Y[i + 2] = DP[i]
    X[i + 1] = (X[i + 1] + DP[i]) % mod
    X[i + N + 2] = (X[i + N + 2] - DP[i]) % mod
for i in range(N, N * 2 + 2):
    C = (C + X[i]) % mod
    DP[i] = (C - Y[i]) % mod
P = sum(DP[N:])
for i in range(N - 1):
    P = (P + DP[i] * (N - 1) * (N - 1)) % mod
print(P)
