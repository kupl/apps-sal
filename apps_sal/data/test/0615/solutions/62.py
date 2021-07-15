n=int(input())
a=list(map(int,input().split()))
accuml=[0]*n
accumr=[0]*n
accuml[0]=a[0]
accumr[0]=a[n-1]
for i in range(n-1):
    accuml[i+1]+=a[i+1]+accuml[i]
    accumr[i+1]+=a[n-i-2]+accumr[i]
ll=0
rr=n-3
ans=10**18
for i in range(1,n-2):
    sl=accuml[i]
    sr=accumr[n-2-i]
    while abs(accuml[ll+1]-sl/2)<abs(accuml[ll]-sl/2):
        ll+=1
    while abs(accumr[rr-1]-sr/2)<abs(accumr[rr]-sr/2):
        rr-=1
    maxi=max(sl-accuml[ll],accuml[ll],sr-accumr[rr],accumr[rr])
    mini=min(sl-accuml[ll],accuml[ll],sr-accumr[rr],accumr[rr])
    ans=min(ans,maxi-mini)
print(ans)
