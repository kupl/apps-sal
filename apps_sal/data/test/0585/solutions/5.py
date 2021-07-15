import sys
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
last=[]
i=n-1
j=m-1
MOD=998244353
failflag=0
while j>=0 and i>=0:
    r=b[j]
    while i>=0:
        if a[i]==r:
            last.append(i)
            break
        if a[i]<r:
            failflag=1
            break
        i-=1
    if i<0:
        break
    j-=1
last.reverse()
if len(last)!=m:
    print(0)
    return
for i in range(last[0]):
    if a[i]<b[0]:
        failflag=1
if failflag==1:
    print(0)
    return
ans=1
for i in range(1,m):
    for j in range(last[i],last[i-1]-1,-1):
        if a[j]<b[i]:
            break
    ans=((last[i]-j)*ans)%MOD
print(ans)
