n,p=map(int,input().split())
s=list(input())

if p==2 or p==5:
  ans=0
  for i,ss in enumerate(s):
    if int(ss)%p==0:
      ans+=i+1
  print(ans)
  return
from collections import Counter
c=Counter()
m=0
c[m]+=1
d=1
s=s[::-1]
for i in range(n):
  m+=int(s[i])*d
  m%=p
  d*=10
  d%=p
  c[m]+=1
ans=0
for v in c.values():
  ans+=v*(v-1)//2
print(ans)
