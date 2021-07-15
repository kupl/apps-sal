n=int(input())
a=list(map(int,input().split()))
dp=[0]#dp[i]=左からi番目までで(i//2)個選んだときの最大値
sum_odd=a[0]

dp.append(0)
for i in range(2,n+1):
  if i%2==1:
    sum_odd+=a[i-1]
    dp.append(max(dp[i-1],dp[i-2]+a[i-1]))
  else:
    dp.append(max(sum_odd,a[i-1]+dp[i-2]))
print((dp[n]))

