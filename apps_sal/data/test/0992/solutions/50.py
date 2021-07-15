import numpy as np
n,s,*a=map(int,open(0).read().split())
mod=998244353
d=np.zeros(s+1,dtype=np.int64)
d[0]=1
for x in a:
	p=d*2
	if x<=s:
		p[x:]+=d[:s-x+1]
	p%=mod
	d=p
print(d[-1])
