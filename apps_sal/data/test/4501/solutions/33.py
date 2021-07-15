N,A = map(int, input().split())
alist = list(map(int, input().split()))

blist = list(map(lambda x:x-A,alist))
sum_plus = 0
sum_minus = 0
for i in blist:
    if i >0:
        sum_plus +=i
    else:
        sum_minus +=i

N=len(alist)
dp = [[0 for i in range(sum_plus - sum_minus + 1)] for j in range(N+1)]
dp[0][0-sum_minus]=1

for i in range(N):
    for j in range(sum_plus - sum_minus+1):
        if j-blist[i] <= (sum_plus - sum_minus):
            dp[i+1][j]=dp[i][j-blist[i]]+dp[i][j]
        else:
            dp[i+1][j]=dp[i][j]

print(dp[N][0-sum_minus]-1)
