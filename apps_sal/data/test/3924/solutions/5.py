from math import floor
n,k=map(int,input().split())
a=list(map(int,input().split()))
ans=0
i=0
rem=0
while i<n:
    if i<n-1:
        if a[i]+rem<=k and rem!=0:
            ans+=1
            i+=1
            rem=0
        else:
            ans+=floor((a[i]+rem)/k)
            rem=(a[i]+rem)%k
            i+=1
    elif i==n-1:
        ans+=floor((a[i]+rem)/k)
        rem=(a[i]+rem)%k
        i+=1
if rem!=0:
    ans+=1
print(ans)
