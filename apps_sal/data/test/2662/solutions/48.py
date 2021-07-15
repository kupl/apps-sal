from bisect import bisect

n=int(input())
a=[0]*n
for i in range(n):
    a[i]=-int(input())

def loopa():

    n=len(a)
    dp = [10**10]*(n+1)
    dp[0] = -10**10
    
    for i in range(n):
        idx = bisect(dp, a[i])
        dp[idx] = min(a[i], dp[idx])

    return dp

dp=loopa()        

print((bisect(dp, 10**10-1)-1))    


