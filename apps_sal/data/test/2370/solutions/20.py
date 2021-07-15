# solution

import io
import math
import scipy.sparse as s,numpy as n

f=n.loadtxt(open(0),skiprows=1)

g=s.csgraph.dijkstra(f)

h=n.where(g,g,1)

print(int(sum(t[j]*(t[j]<t+h[j]).all()for i,t in enumerate(h)for j in range(i)))*(f==g).all()or-1)
