import math
n=int(input())
l=[list(map(int,input().split())) for i in range(n)]
for i in range(n):
  x=math.degrees(math.atan2(l[i][1], l[i][0]))
  l[i]=[x,l[i][0],l[i][1]]
l.sort()
L=l+l
ansL=[]
for i in range(n):
  for j in range(i,n+i):
    ctx=0;cty=0
    for k in range(i,j+1):
      ctx+=L[k][1]
      cty+=L[k][2]
    ansL.append((ctx**2+cty**2)**0.5)
print(max(ansL))
