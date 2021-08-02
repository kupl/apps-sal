import numpy as np

L = input()
mod = 10**9 + 7

DP = np.zeros((len(L) + 1, 2), int)
DP[0][0] = 1

for i in range(len(L)):
    if L[i] == '1':
        DP[i + 1][0] = DP[i][0] * 2
        DP[i + 1][1] = DP[i][0] + DP[i][1] * 3
    else:
        DP[i + 1][0] = DP[i][0]
        DP[i + 1][1] = DP[i][1] * 3
    DP[i + 1] %= mod

print(sum(DP[-1]) % mod)
