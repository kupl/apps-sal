from itertools import accumulate
from collections import Counter
import math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

n,m=map(int,input().split())
s=list(map(lambda x:x%m,list(accumulate(list(map(int,input().split()))))))
s.append(0)
#print(s)
d=Counter(s)
#print(d)
ans=0
for i in d:
    if d[i]>=2:
        ans+=combinations_count(d[i],2)
print(ans)
