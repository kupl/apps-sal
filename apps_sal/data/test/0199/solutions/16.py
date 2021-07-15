import math
n,q=list(map(int,input().split()))
h=list(map(int,input().split()))
t=0
for i in range (n):
    t+=h[i]
if t<q:
    print(-1)
    return
low=min(h)
for i in range (n):
    q-=(h[i]-low)
if q<=0:
    print(low)
    return
low-=math.ceil(q/n)
print(low)

