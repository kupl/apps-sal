from copy import deepcopy
N = input()
A = [ord(N[i]) - ord('0') for i in range(len(N))]
dp = [0, 0]
dp = [deepcopy(dp) for i in range(10 + 1)]
dp = [deepcopy(dp) for i in range(10 + 1)]
dp = [deepcopy(dp) for i in range(len(A) + 1)]
dp[0][10][10][0] = 1
for i in range(len(A)):
    for j in range(10 + 1):
        for k in range(10 + 1):
            for l in range(2):
                lim = 9
                if not l:
                    lim = A[i]
                for d in range(lim + 1):
                    if d == 0 and j == 10 and (k == 10):
                        dp[i + 1][10][10][1] += dp[i][j][k][l]
                    elif j == 10 or j == d:
                        dp[i + 1][d][k][l or d < lim] += dp[i][j][k][l]
                    elif k == 10:
                        if d < j:
                            dp[i + 1][d][j][l or d < lim] += dp[i][j][k][l]
                        else:
                            dp[i + 1][j][d][l or d < lim] += dp[i][j][k][l]
                    else:
                        if d != j and d != k:
                            continue
                        dp[i + 1][j][k][l or d < lim] += dp[i][j][k][l]
ans = 0
for i in range(10):
    for j in range(10 + 1):
        for k in range(2):
            ans += dp[len(A)][i][j][k]
print(ans)
