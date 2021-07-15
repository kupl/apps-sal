N = int(input())
a_ls = list(map(int, input().split()))

dp = [[0,0] for _ in range(N)]
dp[1][0] = a_ls[1] + a_ls[0]
dp[1][1] = -dp[1][0]

for i in range(2,N):
    # flipなしでa_ls[i]を追加
    dp[i][0] = max(dp[i-1][0] + a_ls[i], dp[i-1][1] + a_ls[i])

    # flipありでa_ls[i]を追加
    dp[i][1] = max(dp[i-1][0] - 2*a_ls[i-1] - a_ls[i],dp[i-1][1] + 2*a_ls[i-1] - a_ls[i])

#print(dp)
print((max(dp[-1][0],dp[-1][1])))

