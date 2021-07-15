n,k=list(map(int,input().split()))
arr=list(map(int,input().split()))
ans=0
d={}
for i in range(n):
	x=2
	a=[]
	b=[]
	y=arr[i]
	while x*x<=arr[i]:
		if arr[i]%x==0:
			c=0
			while y%x==0:
				y=y//x
				c+=1
			if c%k>0:
				a.append((x,c%k))
				b.append((x,k-(c%k)))
		x+=1
	if y>1:
		a.append((y,1%k))
		b.append((y,k-(1%k)))
	try:
		ans+=d[tuple(b)]
	except:
		pass
	try:
		d[tuple(a)]+=1
	except:
		d[tuple(a)]=1
print(ans)

