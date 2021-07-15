N=int(input())
*A,=map(int,input().split())

import collections
c = collections.Counter(A)

s=0
for i in c.values():
   s+=i*(i-1)/2

for a in A:
    t=c[a]
    print(int(s-t*(t-1)/2+(t-1)*(t-2)/2))
