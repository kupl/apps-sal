from math import*
n=int(input())
m1=list(map(int,input().split()))
m2=list(map(int,input().split()))
dp=[[0]*2 for i in range(n)]
if n==1:
    print(max(m1[0],m2[0]))
    return
if n==2:
    print(max(m1[0]+m2[1],m2[0]+m1[1]))
    return
dp[0][0]=m1[0]
dp[0][1]=m2[0]
dp[1][0]=m2[0]+m1[1]
dp[1][1]=m2[1]+m1[0]
for i in range(2,n):
    dp[i][0]=max(dp[i-1][1]+m1[i],dp[i-2][1]+m1[i])
    dp[i][1]=max(dp[i-1][0]+m2[i],dp[i-2][0]+m2[i])
print(max(dp[n-1]))

