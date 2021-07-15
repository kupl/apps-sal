n,k=[int(x) for x in input().split()]
a=[int(x) for x in input().split()]
a.sort()
index={}
for i in range(n):
    index[a[i]]=i
dp=[[1]*(k+1) for i in range(n+1)]
for i in range(n+1):
    dp[i][0]=0
for i in range(k+1):
    dp[0][i]=0
for i in range(1,n+1):
    for item in range(5,-1,-1):
            if a[i-1]+item in index:
                counter=index[a[i-1]+item]-i+1
                break
    for j in range(k+1):
        if i>0:
            dp[i][j]=max(dp[i-1][j],dp[i][j])
        
        if j<k:
            dp[i+counter][j+1]=max(dp[i+counter][j+1],dp[i-1][j]+counter+1)
print(dp[n][k])

