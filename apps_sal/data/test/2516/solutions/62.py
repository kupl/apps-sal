n,k=list(map(int,input().split()))
s=list(map(int,list(input())))
ans=0
if k==2 or k==5:
    for i,p in enumerate(s):
        if p%k==0:
            ans+=i+1
else:
    inv10=pow(10,k-2,k)
    inv=10
    total=0
    S=[0]*k
    S[0]=1
    for i,p in enumerate(s):
        inv*=inv10
        inv%=k
        total+=p*inv
        total%=k
        ans+=S[total]
        S[total]+=1
print(ans)

