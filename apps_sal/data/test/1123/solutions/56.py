N,K = map(int,input().split())
mod = 10**9+7
ans = 0

data = [0]*(K+1)
for x in range(K,0,-1):
    p = pow(K//x,N,mod)
    for k in range(2,K//x+1):
        p -= data[k*x]
        p %= mod
    data[x] = p
    ans += x*p
    ans %= mod

###
#print(data)
###
    
print(ans)
