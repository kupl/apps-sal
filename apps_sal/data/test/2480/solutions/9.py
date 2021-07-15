n,k=map(int,input().split())
l=[0]+[i%k-1 for i in list(map(int,input().split()))]
from itertools import accumulate
l=list(accumulate(l))
import collections
d=collections.defaultdict(int)
d[0]+=1
ans=0
for i in range(1,n+1):
    if i>=k:
        d[l[i-k]%k]-=1
    ans+=d[l[i]%k]
    d[l[i]%k]+=1
print(ans)
