N = int(input())
K = int(input())
S = str(N)
L = len(S)
dp0 = [[0 for _ in range(5)] for _ in range(L + 1)]
dp1 = [[0 for _ in range(5)] for _ in range(L + 1)]
dp0[0][0] = 1
dp0[0][1] = 0
for i in range(L):
    D = int(S[i])
    for j in range(4):
        if D > 0:
            dp1[i + 1][j] += dp1[i][j] + dp0[i][j]
            dp0[i + 1][j + 1] += dp0[i][j]
            dp1[i + 1][j + 1] += dp1[i][j] * 9 + dp0[i][j] * (D - 1)
        else:
            dp0[i + 1][j] += dp0[i][j]
            dp1[i + 1][j] += dp1[i][j]
            dp1[i + 1][j + 1] += dp1[i][j] * 9
print((dp0[L][K] + dp1[L][K]))
