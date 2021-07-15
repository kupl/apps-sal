n,h=list(map(int,input().split()))

b = []
t = []
for _ in range(n):
    c,d = list(map(int,input().split()))
    b.append(c)
    t.append(d)


b_max = max(b)
t =sorted(t)

from bisect import bisect_right
from math import ceil
index = bisect_right(t,b_max)

ans=0
for i in range(n-1,index-1,-1):
    h-=t[i]
    ans+=1
    if h<=0:
        print(ans)
        return

cnt = ceil(h/b_max)

print((ans+cnt))



