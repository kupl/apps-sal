N, W = list(map(int, input().split()))
wv = []

for _ in range(N):
    wv.append(tuple(map(int, input().split())))

# dp[i][j] i 番目まで、 重さ j で最大化した価値
# 答え: dp[N][W]
# 初期: dp[0][j] = 0
#       dp[i][0] = 0
#
# dp[i+1][j] = 品物i+1 を使わない場合、 dp[i][j]
#               品物i+1 を使う場合、 dp[i][j-w_{i+1}] + v_{i+1}
# i

memo = {}

def dfs(i, j):
    if (i,j) in memo:
        return memo[(i,j)]

    if i < 0 or j <= 0:
        return 0

    ret = 0
    wi, vi = wv[i]
    if j-wi < 0:
        ret = dfs(i-1, j)
    else:
        ret = max(dfs(i-1, j), dfs(i-1, j-wi) + vi)

    memo[(i,j)] = ret

    return ret

print((dfs(N-1, W)))

