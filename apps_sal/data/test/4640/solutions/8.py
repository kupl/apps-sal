import bisect
t=int(input())
for you in range(t):
    l=input().split()
    n=int(l[0])
    k=int(l[1])
    l=input().split()
    li=[int(i) for i in l]
    l=input()
    li.sort()
    dp=[[0 for i in range(2)]for i in range(n)]
    maxas=[0 for i in range(n)]
    dp[-1][0]=1
    dp[-1][1]=1
    maxas[-1]=1
    for i in range(n-2,-1,-1):
        if(li[i]+k>=li[-1]):
            dp[i][0]=n-i
            dp[i][1]=n-i
            maxas[i]=max(maxas[i+1],dp[i][0])
            continue
        z=bisect.bisect_right(li,li[i]+k)
        dp[i][0]=z-i
        maxas[i]=max(maxas[i+1],dp[i][0])
        dp[i][1]=z-i+maxas[z]
    maxa=0
    for i in range(n):
        maxa=max(maxa,dp[i][0])
        maxa=max(maxa,dp[i][1])
    print(maxa)
