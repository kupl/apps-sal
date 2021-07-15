n=int(input())
a=list(map(int,input().split()))
import heapq as hq
f1=[0]*(3*n)
f1[n-1]=sum(a[:n])
h=a[:n]
hq.heapify(h)
su=f1[n-1]
for i in range(n,2*n):
    cur=a[i]
    x=hq.heappop(h)
    if cur>x:
        su-=x
        su+=cur
        hq.heappush(h,cur)
    else:
        hq.heappush(h,x)
    f1[i]=su
f2=[0]*(3*n)
f2[2*n]=sum(a[2*n:])
su=f2[2*n]
h2=[]
for i in a[2*n:]:
    h2.append(-i)
hq.heapify(h2)
for i in range(2*n-1,n-1,-1):
    cur=a[i]
    x=-1*hq.heappop(h2)
    if cur<x:
        su-=x
        su+=cur
        hq.heappush(h2,-cur)
    else:
        hq.heappush(h2,-x)
    f2[i]=su
ans=-float('inf')
for i in range(n-1,2*n):
    ans=max(ans,f1[i]-f2[i+1])
print(ans)




