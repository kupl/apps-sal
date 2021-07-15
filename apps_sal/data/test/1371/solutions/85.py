##D - Redistribution
##3以上の数字の和でSをつくる組み合わせ
##3以上での動的計画法かな？
S = int(input())
L = list(range(3,S+1))
dp = [1]*(S+1)
if S<3:
    print((0))
else:
    dp[0] = 0
    dp[1] = 0
    dp[2] = 0
    for i in range(3,S+1):
        for j in range(3,S+1-i):
            dp[i+j] += dp[i]

    print((dp[S]%(10**9+7)))

##print(ans)

