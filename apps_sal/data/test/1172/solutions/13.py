S = input()
#dp[i][four] =: i + 1番目まで見たとき,照合したケツがfourとなるものの総数
dp = [[0 for _ in range(4)] for _ in range(len(S)+1 )]
dp[0][0] = 1
mod = 10**9 + 7
for i in range(len(S)):
    if S[i] == 'A' or S[i] == '?':
        dp[i+1][1] += dp[i][0] 
        for k in range(4): dp[i+1][k] += dp[i][k]
    if S[i] == 'B' or S[i] == '?':
        dp[i+1][2] += dp[i][1]
        for k in range(4): dp[i+1][k] += dp[i][k]
    if S[i] == 'C' or S[i] == '?':
        dp[i+1][3] += dp[i][2]
        for k in range(4): dp[i+1][k] += dp[i][k]
    for k in range(4): dp[i+1][k] %= mod
print((dp[len(S)][3]))

