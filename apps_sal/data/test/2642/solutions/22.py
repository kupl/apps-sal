N=int(input())
from collections import defaultdict
import math
d = defaultdict(int)
MOD=10**9+7
for i in range(N):
  a,b=map(int,input().split())
  x=math.gcd(abs(a),abs(b))
  if a==0:
    if b==0:
      k=(0,0)
    else:
      k=(0,1)
  elif b==0:
    k=(1,0)
  else:
    if a<0:
      a,b=-a,-b
    if b<0:
      a,b=a//x,-((-b)//x)
    else:
      a,b=a//x,b//x
    k=(a,b)
  d[k]+=1

ind=defaultdict(int)
index=1
_ans=[1]
for a,b in list(d.keys()):
  if a==b==0:
    continue
  if b<=0:
    _k=(-b,a)
  else:
    _k=(b,-a)
  if d[_k]==0:
    _ans[0]*=pow(2,d[(a,b)])
  else:
    if ind[_k]==0:
      _ans.append(pow(2,d[(a,b)],MOD))
      ind[(a,b)]=index
      index+=1
    else:
      _ans[ind[_k]]+=pow(2,d[(a,b)],MOD)-1
ans=1
for a in _ans:
  ans=ans*a%MOD
print((d[(0,0)]+ans-1+MOD)%MOD)
