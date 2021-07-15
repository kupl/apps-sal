n,k=map(int,input().split())
x=[]
y=[]
xy=[]
for _ in range(n):
  xx,yy=map(int,input().split())
  xy.append((xx,yy))
  x.append(xx)
  y.append(yy)
xx=sorted(x)
yy=sorted(y)
ans=10**20
for sxi in range(n-1):
  for syi in range(n-1):
    for tyi in range(1,n):
      sx,sy,ty=xx[sxi],yy[syi],yy[tyi]
      ax=sorted([xxx for xxx,yyy in xy if sx<=xxx and sy<=yyy<=ty])
      if len(ax)<k:continue
      tx=ax[k-1]
      ans=min(ans,(tx-sx)*(ty-sy))
print(ans)
