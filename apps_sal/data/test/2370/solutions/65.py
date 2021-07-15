import scipy.sparse as s,numpy as n
f=n.loadtxt(open(0),skiprows=1)
g=s.csgraph.dijkstra(f)
h=n.where(g,g,1)
a=0
for i,t in enumerate(h):
  for j in range(i):
    a+=t[j]*(t[j]<t+h[j]).all()
print(int(a)*(f==g).all()or-1)
