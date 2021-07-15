t=int(input())
for r in range(t):
 q=input()
 a=list(map(int,input().split()))
 d=dict()
 for w in a:
  s=0
  while w%2==0:
   w//=2
   s+=1
  if w in list(d.keys()):
   d[w]=max([d[w],s])
  else:
   d[w]=s
 e=0
 for w in list(d.keys()):
  e+=d[w]
 print(e)

