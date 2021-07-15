MOD = 10**9+7
H, W, K = list(map(int, input().split()))
dp = [[0]*W for _ in range(H+1)]
dp[0][0] = 1
for i in range(H):
    for j in range(W):
        for k in range(1<<(W-1)):
            # 2つの横線がつながっていないか調べる
            ok = True
            for l in range(W-2):
                if (k>>l)&1 and (k>>(l+1))&1:
                    ok = False
            if ok:
                if j>=1 and (k>>(j-1))&1:
                    # 左方向に横線をたどるケース
                    dp[i+1][j-1] += dp[i][j]
                    dp[i+1][j-1] %= MOD
                elif j<W-1 and (k>>j)&1:
                    # 右方向に横線をたどるケース
                    dp[i+1][j+1] += dp[i][j]
                    dp[i+1][j+1] %= MOD
                else:
                    # 横線をたどらないケース
                    dp[i+1][j] += dp[i][j]
                    dp[i+1][j] %= MOD
print((dp[H][K-1]))

