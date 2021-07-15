f=range
h,w,k=map(int,input().split())
g=[[int(i) for i in input()] for _ in f(h)]
s=[[0]*-~w for _ in f(h+1)]
for i in f(h):
  for j in f(w):
    s[i+1][j+1]=s[i+1][j]+s[i][j+1]+g[i][j]-s[i][j]
a=h+w
for i in f(2**~-h):
  u=d=l=r=c=0
  e=[]
  for d in f(h):
    if i>>d&1: e+=[(u,d+1)]; c+=1; u=d+1
  e+=[(u,h)]
  for r in f(w):
    if max(s[d][r+1]-s[u][r+1]-s[d][l]+s[u][l] for u,d in e)>k:
      if r==l: break
      c+=1; l=r
  else: a=min(a,c)
print(a)
