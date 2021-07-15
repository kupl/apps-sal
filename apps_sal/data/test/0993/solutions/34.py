from itertools import accumulate
from collections import Counter
n,m=map(int,input().split())
s=[0]+list(map(lambda x:x%m,list(accumulate(list(map(int,input().split()))))))
ans=0
for i in Counter(s).values():
    ans+=(i*(i-1)//2)
print(ans)
