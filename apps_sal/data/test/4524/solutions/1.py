def power(x, y, p) : 
    res = 1     # Initialize result 
  
    # Update x if it is more 
    # than or equal to p 
    x = x % p  
  
    while (y > 0) : 
          
        # If y is odd, multiply 
        # x with result 
        if ((y & 1) == 1) : 
            res = (res * x) % p 
  
        # y must be even now 
        y = y >> 1      # y = y/2 
        x = (x * x) % p 
          
    return res 
n,m=list(map(int,input().split()))
s=input()[::-1]
s1=input()[::-1]
dp=[0 for i in range(max(n,m)+1)]
mod=998244353
for i in range(m-1,-1,-1):
    if s1[i]=='1':
        dp[i]=(dp[i+1]+1)%mod
    else:
        dp[i]=dp[i+1]
ans=0
for i in range(n):
    if s[i]=='1':
        ans=(ans+(dp[i]*power(2,i,mod))%mod)%mod
        
print(ans)

