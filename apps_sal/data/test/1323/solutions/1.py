n,m=list(map(int,input().split())) 

a=list(map(int,input().split()))
b=list(map(int,input().split()))
# asum=0
# bsum=0
a.sort()
b.sort()
asum=sum(a)
bsum=sum(b)
ans=9999999999999999999999999999999999999999
# print(a[0])
le=0
for i in range(0,n):
    tmp=le+(n-i)*(bsum)
    ans=min(ans,tmp)
    le=le+a[i]
    
le=0    
for i in range(0,m):
    tmp=le+(m-i)*(asum)
    ans=min(ans,tmp)
    le=le+b[i]
    
print(ans)

