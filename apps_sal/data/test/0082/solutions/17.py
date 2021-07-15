x,y=list(map(int,input().split()))
a=list(map(int,input().split()))
n=0
d=0
for i in range(x):
	n=n+a[i]
while round((n+0.01)/x)!=y:
	n=n+y
	x=x+1
	d+=1
print(d)

