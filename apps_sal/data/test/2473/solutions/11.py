n,h=map(int,input().split())
p,x,y=[],[],[]
z=float("inf")
for i in range(n):
  a,b=map(int,input().split())
  p.append((a,b))
  x.append(a)
  y.append(b)
x.sort()
y.sort()
for i in range(n-1):
  for j in range(i,n):
    for k in range(n-1):
      lx,rx,dy=x[i],x[j],y[k]
      c=0
      t=[]
      for a,b in p:
        if x[i]<=a<=x[j] and y[k]<=b:c+=1;t.append(b)
      if h<=c:z=min(z,(x[j]-x[i])*(sorted(t)[h-1]-y[k]))
print(z)
