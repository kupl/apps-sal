x,y=map(int, input().split())
import math
ans=0

def conbi(n,r,mod):
    ue=1
    for i in range(n-r+1,n+1):
        ue*=i
        ue%=mod
 
    sita=1
 
    for i in range(1,r+1):
        sita*=i
        sita%=mod
 
    sita=pow(sita,mod-2,mod)
 
    return (ue*sita)%mod

for a in range(x+1):
    b=(x-a)/2
    if b-int(b)==0:
        b=int(b)
        if y==2*a+b:
            ans+=conbi(a+b,a,10**9+7)

print(ans)
