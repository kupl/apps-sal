import math
from functools import reduce
n=int(input())
a=list(map(int,input().split()))
ans=reduce(math.gcd,a)
if ans>1:
  print("not coprime")
  return
maxn=10**6+10
li=[i for i in range(maxn+1)]
p=2
while p*p<=maxn:
  if li[p]==p:
    for q in range(2*p,maxn,p):
      if li[q]==q:
        li[q]=p
  p+=1
ans=[0]*(maxn+1)
for i in a:
  bk=0
  while i>1:
    wk=li[i]
    i//=wk
    if ans[wk]==0 and bk!=wk:
      ans[wk]=1
      bk=wk
    elif bk==wk:
      continue
    else:
      print("setwise coprime")
      return
print("pairwise coprime")
