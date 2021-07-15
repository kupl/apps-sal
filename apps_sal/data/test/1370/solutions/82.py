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
  while d<h:
    d+=1
    if i>>d-1&1: e+=[(u,d)]; c+=1; u=d
  e+=[(u,h)]
  while r<w:
    if max(s[d][r+1]-s[u][r+1]-s[d][l]+s[u][l] for u,d in e)>k:
      if r==l: break
      c+=1; l=r
    r+=1
  else: a=min(a,c)
print(a)
