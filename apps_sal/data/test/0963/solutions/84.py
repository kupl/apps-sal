n, k = map(int, input().split())
L = [0 for i in range(k)]
R = [0 for i in range(k)]
for i in range(k):
    L[i], R[i] = map(int, input().split())

DP = [0 for i in range(n + 1)]
S = [0 for i in range(n + 1)]
mod = 998244353
DP[1] = 1
S[1] = 1
for i in range(2, n + 1):
    for j in range(k):
        imin, imax = max(0, i - R[j]), max(0, i - L[j])
        DP[i] = (DP[i] + S[imax] - S[imin - 1]) % mod
    S[i] = (S[i - 1] + DP[i]) % mod

print(DP[n])
