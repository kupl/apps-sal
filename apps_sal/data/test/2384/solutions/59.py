N = int(input())
A = list(map(int, input().split()))
k = 1+N%2 # 余分なxを入れる個数
INF = 10**18
# dp: i番目まで見たときに、j個の余分なxを入れた時の、和の最大値
dp = [[-INF for _ in range(4)] for _ in range(202020)]
dp[0][0] = 0
for i in range(N):
    for j in range(k+1):
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]) # xを一つ挿入する=>今見てる数字をスキップする
        now = dp[i][j]
        if (i+j)%2==0:
            now += A[i]
        dp[i+1][j] = max(dp[i+1][j], now)
print(dp[N][k])
