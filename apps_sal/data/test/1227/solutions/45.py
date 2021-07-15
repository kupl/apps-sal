N=list(map(int,input()))
K=int(input())
L = len(N)
dp = [[[0]*(L+1) for _ in range(4)] for _ in range(2)]
dp[0][0][0] = 1
for i in range(2):
    for j in range(4):
        for k in range(L):
            for d in range(10 if i else N[k]+1):
                fl = 1 if i == 1 or d < N[k] else 0
                cnt = j+1 if d != 0 else j
                if cnt > K:
                    continue
                dp[fl][cnt][k+1] += dp[i][j][k]
print(dp[0][K][L]+dp[1][K][L])
