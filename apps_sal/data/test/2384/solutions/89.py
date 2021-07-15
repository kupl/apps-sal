n = int(input())
a = list(map(int, input().split()))

# dp[i][k] 列iを選択し、k個持っているときの最大値
# kは(i-1)//2 or i//2 or (i+1)//2
# それぞれki=0,1,2とする。
# 最大でも4マス前まで(oxxxo)
# iが奇数
# dp[i+2][0]=Ai + max(dp[i][0], dp[i][1], dp[i-1][1],  dp[i-2][2])
# dp[i+2][1]=dp[i+2][0]
# dp[i+2][2]=Ai + max(dp[i][2])
# iが偶数
# dp[i+2][0]=0
# dp[i+2][1]=Ai + max(dp[i][1], dp[i][2], dp[i-1][2])
# dp[i+2][2]=dp[i+2][1]

dp = [[0 for i in range(3)] for j in range(n)]
ans = 0

dp[0][2] = a[0]
ans = dp[0][2]
dp[1][0] = 0
dp[1][1] = a[1]
dp[1][2] = a[1]
ans = max([ans, dp[1][1]])

if n == 2:
    print(ans)
else:
    for i in range(2, n):
        if (i + 1) % 2 == 0:
            dp[i][0] = 0
            dp[i][1] = a[i] + max(dp[i - 2][1], dp[i - 3][2])
            dp[i][2] = dp[i][1]
        else:
            if i > 2:
                dp[i][0] = a[i] + max(dp[i - 2][0], dp[i - 3][1], dp[i - 4][2])
            else:
                dp[i][0] = a[i] + dp[i - 2][0]
            dp[i][1] = dp[i][0]
            dp[i][2] = a[i] + dp[i - 2][2]
        
    if n % 2 == 0:
        print(max(dp[-1][1],dp[-2][2]))
    else:
        print(max(dp[-1][0],dp[-2][1],dp[-3][2]))
