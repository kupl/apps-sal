from collections import defaultdict as df
import heapq
import bisect 
import math
from itertools import combinations,permutations
from collections import deque

n,k=list(map(int,input().split()))
a=list(map(int,input().rstrip().split()))
ans=deque()
p=df(int)
for i in range(n):
    p[i]=0
for i in a:
    if p[i]>0:
        pass
    
    else:
        if len(ans)>=k:
            g=ans.pop()
            ans.appendleft(i)
            p[i]+=1
            p[g]-=1
        else:
            ans.appendleft(i)
            p[i]+=1
print(len(ans))
print(*ans)
