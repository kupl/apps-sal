mod = 10**9 + 7
n,k= [int(i) for i in input().split()]

d = [0] * (k + 1)

for i in range(1,k+1):
    d[i] = pow(k//i,n,mod)
    
    
for i in range(k,0,-1):
    for j in range(2*i,k+1,i):
        d[i] -= d[j]
        d[i] %= mod
        
ans = 0 
for idx,i in enumerate(d):
    ans += (idx) * i
    ans %= mod

print(ans)

