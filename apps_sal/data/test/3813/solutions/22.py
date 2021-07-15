n=int(input())
p,x=[list(map(int,input().split())) for _ in [0]*2]
g=[[] for _ in [0]*n]
[g[j-1].append(i+1) for i,j in enumerate(p)]
d=[0]*n
q=[0]
while q:
 r=q.pop()
 for i in g[r]:
  if i!=0:
   d[i]=d[p[i-1]-1]+1
   q.append(i)
d=sorted([[-j,i] for i,j in enumerate(d)])
m=[[i,0] for i in x]
a,b=10003,5001
for _,i in d:
 y=x[i]+1
 e=[a]*y
 e[0]=0
 for j in g[i]:
  f=[a]*y
  p,q=m[j]
  for k in range(y-p):
   if e[k]!=a:f[k+p]=min(f[k+p],e[k]+q,b)
  for k in range(y-q):
   if e[k]!=a:f[k+q]=min(f[k+q],e[k]+p,b)
  e=f
 m[i][1]=min(e)
 if min(e)==a:
  print("IMPOSSIBLE")
  break
else:print("POSSIBLE")
