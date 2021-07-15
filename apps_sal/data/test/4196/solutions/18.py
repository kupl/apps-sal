import math
n=int(input())
a=list(map(int, input().split()))
alist=[]
gcd1=a[0]
for i in range(0,n):
  gcd1=math.gcd(gcd1,a[i])
  alist.append(gcd1)
blist=[]
gcd2=a[n-1]
for i in range(n-1,-1,-1):
  gcd2=math.gcd(gcd2,a[i])
  blist.append(gcd2)
clist=[alist[n-2],blist[n-2]]
for i in range(n-2):
  clist.append(math.gcd(alist[i],blist[n-i-3]))
print(max(clist))
