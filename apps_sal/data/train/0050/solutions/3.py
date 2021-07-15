from math import *
for _ in range(int(input())):
	n=int(input())
	a=list(map(int,input().split()))
	z=a.count(1)-a.count(2)
	c=a[:n]
	d=a[n:]
	jk={0:0}
	b=0
	for i in range(n):
		x=d[i]
		if x==1:
			b-=1
		else:
			b+=1
		if b not in jk:
			jk[b]=i+1
	ans=1000000
	b=0
	i=1
	if z==0:
		ans=0
	for x in c[::-1]:
		if x==1:
			b-=1
		else:
			b+=1
		if -z-b in jk:
			ans = min(ans,i+jk[-z-b])
		i+=1
	if -z in jk:
		ans=min(ans,jk[-z])
	print(ans)

