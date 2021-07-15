S = input()
N = len(S)
K = int(input())

dp = [[[0] * 2 for _ in range(4)] for _ in range(N + 10)]
dp[0][0][0] = 1

for i, s in enumerate(S):
    nd = int(s)
    for j in range(K+1):
        for k in range(2):
            for d in range(10):
                ni = i + 1
                nj = j
                nk = k
                if d != 0:
                    nj += 1
                if nj > K:
                    continue
                if nk == 0:
                    if d > nd:
                        continue
                    if d < nd:
                        nk += 1
                dp[ni][nj][nk] += dp[i][j][k]

print(dp[N][K][0]+dp[N][K][1])
