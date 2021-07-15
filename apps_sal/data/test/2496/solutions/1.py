n=int(input())
l=list(map(int,input().split()))
m=max(l)

from math import gcd
g=gcd(l[0],l[1])
for i in range(2,n):
  g=gcd(g,l[i])
if g!=1:
  print('not coprime')
  return

prime=[True]*(m+1)
prime[0]=False
prime[1]=False
d=[0]*(m+1)
for i in range(2,int(m**0.5)+1):
  if prime[i]:
    for j in range(i*2,m+1,i):
      prime[j]=False
      d[j]=i
s=[i for i in range(m+1) if prime[i]]
for ss in s:
  d[ss]=ss

sl=set()
for i in range(n):
  div=set()
  ll=l[i]
  while ll>1:
    div.add(d[ll])
    ll//=d[ll]
  div=list(div)
  for dd in div:
    if dd not in sl:
      sl.add(dd)
    else:
      print('setwise coprime')
      return

print('pairwise coprime')
