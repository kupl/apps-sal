n,m,k = list(map(int,input().split()))
lis = sorted(map(int,input().split()))+[1000000000000000]
j=zer=ans=0
for i in range(n):
    if lis[i]==0:
        zer-=1
        continue
    j=max(j,i)
    while j<=n and lis[j]-lis[i]<m:
        j+=1
    if j-i-zer>=k:
        a=j-1
        ext=j-i-zer-k+1
        t=0
        while a>=0 and ext>0:
            if lis[a]!=0:
                lis[a]=0
                t+=1
                zer+=1
                ext-=1
            a-=1
        ans+=t
    if lis[i]==0:
        zer-=1       
print(ans)            



