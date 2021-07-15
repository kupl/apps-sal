N,K,*l=map(int,open(c:=0).read().split())
for a,b in sorted(zip(l[::2],l[1::2])):
	if(c:=c+b)>=K:break
print(a)
