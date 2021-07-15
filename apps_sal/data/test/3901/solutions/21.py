n=int(input())
l=list(map(int,input().split()))
cnt=l.count(1)
if cnt>0:
    print(n-cnt)
    return
import math
m=n+1
for i in range(n):
    g=l[i]
    for j in range(n-i):
        g=math.gcd(g,l[i+j])
        if g==1:
            m=min(m,j)
if m==n+1:
    print(-1)
else:
    print(m+n-1)

