from heapq import *
from collections import defaultdict
def D(v,g):
	h,p,o=[],defaultdict(lambda:1e99),[]
	heappush(h,(0,v))
	while h:
		l,w=heappop(h)
		if w in p:continue
		p[w]=l
		o.append(w)
		for u,L in g[w]:
			heappush(h,(L+l,u))
	return p,o
n,m,s,t=list(map(int,input().split()))
r=[]
g={i+1:[] for i in range(n)}
G={i+1:[] for i in range(n)}
for _ in range(m):
	a,b,l=list(map(int,input().split()))
	r.append((a,b,l))
	g[a].append((b,l))
	G[b].append((a,l))
S,o=D(s,g)
T,_=D(t,G)
L=S[t]
H={v:[w for w,l in e if S[v]+T[w]+l==L] for v,e in list(g.items())}
B,A=set(),{s}
for v in o:
	if not H[v]:continue
	if 1==len(A)==len(H[v]):B.add(v)
	A.update(H[v])
	A.remove(v)
print('\n'.join("YES" if a in B and S[a]+T[b]+l==L else "CAN "+str(S[a]+T[b]+l-L+1) if S[a]+T[b]+1<L else "NO" for a,b,l in r))

