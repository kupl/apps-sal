from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import dijkstra
import numpy as np

N,M,S=map(int,input().split())

Us=[0]*M
Vs=[0]*M
As=[0]*M
Bs=[0]*M
for i in range(M):
    Us[i],Vs[i],As[i],Bs[i] = map(int,input().split())
    Us[i] -= 1
    Vs[i] -= 1

# ---
V={}
Ns = max(As)*N
Nv=N*(Ns+1)
cnt=0
for i in range(N):
    for ns in range(Ns+1):
        V[(i,ns)]=cnt
        cnt+=1

row=[]
col=[]
data=[]

if S > Ns:
    S = Ns

# U <-> V
for _ in range(M):
    u = Us.pop()
    v = Vs.pop()
    a = As.pop()
    b = Bs.pop()
    #
    for i in range(Ns+1): # i = 0,..,Ns
        ns_s = Ns - i
        ns_g = ns_s - a
        if ns_g >= 0:
            # U -> V
            row.append( V[(u,ns_s) ])
            col.append( V[(v,ns_g)] )
            data.append( b )
            # V -> U
            row.append( V[(v,ns_s) ])
            col.append( V[(u,ns_g)] )
            data.append( b )

# -----

for i in range(N):
    c,d = map(int,input().split())
    for j in range(Ns): # j = 0,...,Ns-1
        ns_s = j
        ns_g = j + c
        if ns_g > Ns:
            ns_g = Ns
        row.append( V[(i,ns_s) ])
        col.append( V[(i,ns_g)] )
        data.append( d )

graph=coo_matrix((data, (row, col)), shape=(Nv,Nv))

s=V[(0,S)]
dist_matrix = dijkstra(csgraph=graph, directed=True, indices = s)

for i in range(1,N):
    ans = min([dist_matrix[i*(Ns+1)+v] for v in range(Ns+1)])
    print(int(ans))
