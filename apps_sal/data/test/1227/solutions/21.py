N = input()
K = int(input())
nSize = len(N)

dp = [[[0] * 2 for _ in range(K + 1)] for _ in range(nSize + 1)]
dp[0][0][0] = 1

for i in range(nSize):
    for j in range(K + 1):
        for k in range(2):
            for l in range(10):
                ni = i + 1
                nj = j
                nk = k
                if l != 0: nj += 1
                if nj > K: continue
                if k == 0:
                    if l > int(N[i]): continue
                    if l < int(N[i]): nk = 1
                dp[ni][nj][nk] += dp[i][j][k]

print(dp[nSize][K][0] + dp[nSize][K][1])
