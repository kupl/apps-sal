from collections import *
ans=0
c=Counter()
n=int(input())
for x in input().split(): c[int(x)]+=1
while len(c)>1:
    ans+=len(c)-1
    for x in set(c): 
        c[x]-=1
        if c[x]==0: del c[x]
print(ans)

