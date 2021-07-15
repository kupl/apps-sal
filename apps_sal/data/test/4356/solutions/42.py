import sys
stdin=sys.stdin

ip=lambda: int(sp())
fp=lambda: float(sp())
lp=lambda:list(map(int,stdin.readline().split()))
sp=lambda:stdin.readline().rstrip()
yp=lambda:print('Yes')
np=lambda:print('No')

n,m=lp()
ans=[]
for _ in range(n):
  s=list(sp())
  ans.append(s)

next=[]
for _ in range(m):
  p=list(sp())
  next.append(p)
  
ok=0
count=0
for x in range(n-m+1):
  for y in range(n-m+1):
    ch=0
    for e in range(m):
      for f in range(m):
        if ans[x+e][y+f]==next[e][f]:
          ch+=1
        if ch==m*m:
          ok+=1
  
if ok==0:
  print('No')
else:
  print('Yes')
        
  
