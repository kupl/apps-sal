n,m=map(int,input().split())
a=list(map(int,input().split()))

for i in range(1,n):
  a[i]+=a[i-1]
a=[0]+a
b=[q%m for q in a]
from collections import Counter
c=Counter(b).items()
ans=0
for i,j in c:
  ans+=(j*(j-1)//2)
print(ans)
