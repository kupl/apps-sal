N,K,*l=map(int,open(0).read().split())
for a,b in sorted(zip(*[iter(l)]*2)):
	if(K:=K-b)<1:break
print(a)
