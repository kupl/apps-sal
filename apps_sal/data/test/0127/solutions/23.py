x,y=list(map(int,input().split()))
n=0
d=[0]*x
f=[]
for i in range(x):
	a,b=list(map(int,input().split()))
	if b<a:
		n=n+b
	else:
		n=n+a
	if b>a:
		if a*2<b:
			d[i]=a
		else:
			d[i]=b-a
if d!=f:
	d.sort()
	for i in range(1,y+1):
		n=n+d[-i]
print(n)

