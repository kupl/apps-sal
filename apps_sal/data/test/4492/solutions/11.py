N,x=map(int,input().split())
a=list(map(int,input().split()))
ans=0
for i in range(1,N):
    tmp=a[i-1]+a[i]
    if tmp>x:
        ans+=tmp-x
        if a[i]>=tmp-x:
            a[i]-=tmp-x
        else:
            a[i]=0
print(ans)
