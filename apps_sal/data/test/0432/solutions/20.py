n=int(input())
c=list(map(int,input().split()))
a=list(map(int,input().split()))

ans=0
v=[False for i in range(n)]
for i in range(n):
	if v[i]:continue
	p=set()
	pl=[]
	s=set([i])
	t=True
	while s and t:
		x=s.pop()
		v[x]=True
		p.add(x)
		pl.append(x)
		nex=a[x]-1
		s.add(nex)
		if nex in p:
			j=pl.index(nex)
			za=s.pop()
		elif v[nex]:t=False;za=s.pop()
		
	
	if not t:continue
	an=float("INF")
	for k in range(j,len(pl)):
		an=min(c[pl[k]],an)
	ans+=an
print(ans)
