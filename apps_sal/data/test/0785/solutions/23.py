from math import sqrt
n, a, b=map(int, input().split())
p, x, y=a*b, a, b
n*=6
if n>p:
	i=min(x, y)
	j=min((n//max(x, y)), int(sqrt(n)))+1
	p=n*(a+b)
	for e in range(i, j):
		k=(n+e-1)//e
		if e*k<p:
			p=e*k
			x=e
			y=k
			if p==n:
				break
if (a>b and x<y) or (a<b and x>y):
	x, y=y, x
print(p)
print(x, y)
