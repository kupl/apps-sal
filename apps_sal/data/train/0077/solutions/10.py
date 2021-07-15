import sys
from math import inf as inf
for _ in range(int(input())):
    n=int(sys.stdin.readline())
    dp=[[inf,inf,inf] for i in range(n+1)]
    a=[]
    for i in range(n):
        a.append(list(map(int,sys.stdin.readline().split())))
    dp[0][0]=0
    dp[0][1]=a[0][1]
    dp[0][2]=2*a[0][1]
    for i in range(1,n):
        for j in range(3):
            for k in range(3):
                if a[i][0] + j != a[i-1][0] + k:
                    dp[i][j]=min(dp[i][j],dp[i-1][k] + j*a[i][1])
    # print(dp)                
    print(min(dp[n-1]))                
