from heapq import heappop, heappush
n=int(input())
a=list(map(int,input().split()))
l=[0]*(n+1)
r=[0]*(n+1)
s=sum(a[:n])
t=sum(a[-n:])
l[0]=s
r[~0]=t
h=[]
H=[]
for i in range(n):
    heappush(h,a[i])
    heappush(H,-a[~i])
for i in range(n):
    s+=a[n+i]
    t+=a[~(n+i)]
    heappush(h,a[n+i])
    heappush(H,-a[~(n+i)])
    s-=heappop(h)
    t+=heappop(H)
    l[i+1]=s
    r[~(i+1)]=t
print(max(l[i]-r[i] for i in range(n+1)))
