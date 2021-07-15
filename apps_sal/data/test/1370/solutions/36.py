h,w,k=map(int,input().split())
g=[[int(c) for c in input()] for _ in range(h)]
s=[[0]*(w+1) for _ in range(h+1)]
for i in range(h):
  for j in range(w):
    s[i+1][j+1]=s[i+1][j]+s[i][j+1]+g[i][j]-s[i][j]
ssum=lambda u,d,l,r:s[d][r]-s[u][r]-s[d][l]+s[u][l]
a=h+w
for i in range(2**(h-1)):
  e=[]
  u=d=ch=0
  for j in range(h):
    d+=1
    if i>>j&1<1:
      e+=[(u,d)]
      if d<h:
        ch+=1
        u=d
  l=r=cw=0
  while r<w:
    if max(ssum(u,d,l,r+1) for u,d in e)>k:
      if r==l: break
      cw+=1
      l=r
    r+=1
  else:
    a=min(a,ch+cw)
print(a)
