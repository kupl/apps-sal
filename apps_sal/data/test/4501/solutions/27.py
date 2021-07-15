import sys

n,a=list(map(int, input().split()))
cards=list(map(int, input().split()))

integers=[x-a for x in cards]
cards.append(a)
f=max(cards)*n


dp=[[0 for i in range(n+1)] for j in range(2*f+1) ]

for y in range(n+1):
    for x in range(2*f+1):
        if y==0 and x==f:
            dp[x][y]=1
        elif y>0 and (x-integers[y-1]<0 or x-integers[y-1]>2*f):
            dp[x][y]=dp[x][y-1]
        elif y>0 and x-integers[y-1]>=0 and x-integers[y-1]<=2*f:
            dp[x][y]=dp[x-integers[y-1]][y-1]+dp[x][y-1]
        else:
            dp[x][y]=0
print((dp[f][n]-1))


