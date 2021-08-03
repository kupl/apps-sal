import numpy as np

N = input()
K = int(input())

n = len(N)
dp0 = np.zeros((n, K + 1), np.int64)
dp1 = np.zeros((n, K + 1), np.int64)

dp0[0, 0] = 1
dp0[0, 1] = int(N[0]) - 1
dp1[0, 1] = 1
for i, d in enumerate(N[1:]):
    dp0[i + 1] += dp0[i]
    dp0[i + 1, 1:] += dp0[i, :-1] * 9
    if int(d) == 0:
        dp1[i + 1] = dp1[i]
    elif int(d) == 1:
        dp0[i + 1] += dp1[i]
        dp1[i + 1, 1:] = dp1[i, :-1]
    elif int(d) >= 2:
        dp0[i + 1] += dp1[i]
        dp0[i + 1, 1:] += dp1[i, :-1] * (int(d) - 1)
        dp1[i + 1, 1:] = dp1[i, :-1]

print((dp0[-1, K] + dp1[-1, K]))
