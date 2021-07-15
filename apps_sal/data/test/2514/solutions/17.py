N=int(input())
*A,=map(int,input().split())
Q=int(input())
BC=[list(map(int,input().split())) for _ in range(Q)]

import collections
c = collections.Counter(A)
s=sum(A)

for i,j in BC:
    s=s-i*c[i]+j*c[i]
    print(s)
    c[j]+=c[i]
    c[i]=0
