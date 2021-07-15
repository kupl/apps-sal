import sys
import math
from collections import defaultdict
n,k=list(map(int,sys.stdin.readline().split()))
a=list(map(int,sys.stdin.readline().split()))
l=[0 for _ in range(n)]
for i in range(n):
    l[i]=a[i]%k
ans=set()
ans.add(0)
vis=defaultdict(int)
x=0
for i in range(n):
    x=math.gcd(x,l[i])
st=0
x=math.gcd(x,k)
while st*x<k and x!=0:
    ans.add(st*x)
    st+=1
print(len(ans))
res=list(ans)
res.sort()
print(*res)

