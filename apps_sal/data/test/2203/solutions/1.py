h,q=list(map(int,input().split()))
d=[(2**h,0),(2**(h-1),0)]
for _ in range(q):
	i,l,r,a=list(map(int,input().split()))
	l,r=l*2**(h-i),(r+1)*2**(h-i)
	d.extend([[(l,1),(r,-1)],[(0,1),(l,-1),(r,1)]][a])
s=0
l=0
d=sorted(d)
for (a,x),(b,_) in zip(d,d[1:]):
	s+=x
	if a!=b and s==0:q=a;l+=b-a
print(("Game cheated!",q,"Data not sufficient!")[min(l,2)])

