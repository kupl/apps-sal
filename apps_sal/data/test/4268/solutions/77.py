import numpy as np
from itertools import combinations
n,d=map(int,input().split())
l= [np.array(input().split() ,dtype=np.int64) for _ in range(n)]
ans=0
dist=0
for a,b in combinations(l,2):
    dist=((a-b)**2).sum()
    for j in range(dist+1):
        if  j**2 == dist:
            ans+=1
            continue
print(ans)
