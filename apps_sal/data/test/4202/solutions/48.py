L,R=map(int,input().split())
mod=2019
ans=2018
if R-L>=mod:
    print(0)
else:
    R%=mod
    L%=mod
    if R<=L:
        R+=mod
    for i in range(L+1,R+1):
        for j in range(L,i):
            ans=min(ans,i*j%mod)
    print(ans)
