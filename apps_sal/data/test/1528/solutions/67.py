n, x = list(map(int, input().split()))

dp = [1]*(n+1)
res = 0

for i in range(1,n+1):
    dp[i] = dp[i-1]*2+3

for j in range(n,1,-1):
    if dp[j] ==x:
        res += (dp[j]+1) //2
        x =0        
    elif dp[j-1]+2 <= x :
        res += 1 + (dp[j-1]+1)//2
        x -= dp[j-1]+2
    elif dp[j-1]+1 ==x:
        res += (dp[j-1]+1)//2
        x = 0
    else:
        x -=1
    
    if x ==0:
        break
        
if x ==5:
    res += 3
elif x ==0:
    pass
else:
    res +=x-1

print(res)

