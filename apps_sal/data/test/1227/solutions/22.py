N = input()
K = int(input())

keta = len(N)

dp = [[[0]*(keta+1) for _ in range(K+1)] for _ in range(2)]

for i in range(keta-1):
    dp[0][0][i] = 1
dp[0][1][0] = int(N[0])-1
dp[1][1][0] = 1

for i in range(1, K+1):
    for j in range(i-1, keta):
        x = int(N[j])
        dp[0][i][j] += dp[0][i][j-1] + dp[0][i-1][j-1]*9
        dp[0][i][j] += dp[1][i][j-1] if N[j]!="0" else 0
        dp[0][i][j] += dp[1][i-1][j-1] * max(int(N[j])-1, 0)

        dp[1][i][j] += dp[1][i][j-1]*int(N[j]=="0")
        dp[1][i][j] += dp[1][i-1][j-1]*int(N[j]!="0")

print(dp[0][-1][-2] + dp[1][-1][-2])
