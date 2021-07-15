n=int(input())
ans=[]
l=[int(i) for i in input().split()]
for i in range(n):
    for j in range(i+1,n):
        ans.append(l[i]+l[j])
#print(ans)
from collections import Counter
c=Counter(ans)
maxi=0 
for i in c:
    if c[i]>maxi:
        maxi=c[i]
        ans=i 

print(maxi)
