N,K,*L=list(map(int,open(0).read().split()))
S=sorted([(d,t)for t,d in zip(*[iter(L)]*2)],reverse=True)
In=set()
X=0
uni=[]
dub=[]
for d,t in S:
	if t not in In:
		In.add(t)
		uni.append(d)
		X+=1
		if X==K:
			break
	else:
		dub.append(d)
det=sum(dub[:K-X])
dub=dub[K-X:]
for d in dub:
	if uni[-1]+2*X-1<=d:
		uni.pop()
		X-=1
		det+=d
	else:
		break
print((sum(uni)+det+X**2))


