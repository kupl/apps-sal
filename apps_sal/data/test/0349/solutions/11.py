n , m = list(map(int,input().split()))
m1 = [list(map(int,input().split())) for i in range(n)]
m2 = [list(map(int,input().split())) for i in range(n)]
import sys
for i in range(n - 1):
	for j in range(m - 1):
		a, b = m1[i][j], m2[i][j]
		c, d = m1[i+1][j], m2[i+1][j]
		e, f = m1[i][j+1], m2[i][j+1]
		if a > b:
			a,b=b,a
		if c>d:
			c,d=d,c
		if e>f:
			e,f=f,e
		if b>=d:
			print("Impossible")
			return
		else:
			if a >=c:
				print("Impossible")
				return
		if b>=f:
			print("Impossible")
			return
		else:
			if a >=e:
				print("Impossible")
				return
for i in range(n-1):
	j = m - 1
	a, b = m1[i][j], m2[i][j]
	c, d = m1[i+1][j], m2[i+1][j]
	if a > b:
		a,b=b,a
	if c>d:
		c,d=d,c
	if b>=d:
			print("Impossible")
			return
	else:
		if a >=c:
			print("Impossible")
			return
for j in range(m-1):
	i = n - 1
	a, b = m1[i][j], m2[i][j]
	e, f = m1[i][j+1], m2[i][j+1]
	if a > b:
		a,b=b,a
	if e>f:
		e,f=f,e
	if b>=f:
			print("Impossible")
			return
	else:
		if a >=e:
			print("Impossible")
			return
print("Possible")
