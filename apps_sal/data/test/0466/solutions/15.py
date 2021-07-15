c,d = [int(x) for x in input().strip().split()]
n,m = [int(x) for x in input().strip().split()]
k = int(input().strip())

t = n*m-k
if t<=0:
    print(0)
else:
    dp = [0]*(t+1)
    for i in range(1,t+1):
        dp[i]=min(dp[i-1]+d, c+dp[max(0,i-n)])
    print(dp[t])
