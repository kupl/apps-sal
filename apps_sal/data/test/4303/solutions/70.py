n,k=list(map(int,input().split()))
x=list(map(int,input().split()))
a=[x[i] for i in range(n) if x[i]<0]
b=[x[i] for i in range(n) if x[i]>=0]
na=len(a)
nb=len(b)
if 0 in x:
    k-=1
    b=[x[i] for i in range(n) if x[i]>0]
    nb=nb-1

if k==0:
    print((0))
    return
ans=10**10
if na>=k:
    ans=-a[-k]

if nb>=k:
    ans=min(ans,b[k-1])

if nb==0:
    print((-a[-k]))
    return

if na==0:
    print((b[k-1]))
    return

for i in range(1,nb+1):
    m=k-i
    if m>na or m<0:
        continue
    elif 0<m<=na:
        ans=min(ans,min(b[i-1]-2*a[-m],2*b[i-1]-a[-m]))
    elif m==0:
        ans=min(ans,b[k-1])
print((ans if k!=0 else 0))

