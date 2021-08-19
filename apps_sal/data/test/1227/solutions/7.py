import math


def solve(sN):
    dp = [[[0] * 105 for _ in range(4)] for _ in range(2)]
    dp[0][0][0] = 1
    for i in range(len(sN)):
        for j in range(4):
            for k in range(2):
                nd = int(sN[i])
                for d in range(10):
                    ni = i + 1
                    nj = j
                    nk = k
                    if d != 0:
                        nj += 1
                    if nj > K:
                        continue
                    if k == 0:
                        if d > nd:
                            continue
                        if d < nd:
                            nk = 1
                    dp[nk][nj][ni] += dp[k][j][i]
    ans = dp[0][K][len(sN)] + dp[1][K][len(sN)]
    return ans


sN = input()
K = int(input())
lenN = len(sN)
ans = solve(sN)
print(ans)
