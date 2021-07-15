def check(x):
    j=0
    for i in range(n):
        if j>=k:
            return False
        while abs(b[j]-a[i])+abs(b[j]-p)>x:
            j+=1
            if j>=k:
                return False
        j+=1
    return True
n,k,p=list(map(int,input().split()))
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
b.sort()
l=0
r=10**18
ans=-1
while l<=r:
    mid=l+(r-l)//2
    if check(mid):
        r=mid-1
        ans=mid
    else:
        l=mid+1
print(ans)



