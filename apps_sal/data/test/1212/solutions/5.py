n,k=list(map(int,input().split()))


L=list(map(int,input().split()))

s=sum(L[0:k])

ind=0
minn=s
ans=0
for i in range(k,n):
    s+=L[i]
    s-=L[ind]
    ind+=1
    if(s<minn):
        minn=s
        ans=ind
print(ans+1)

