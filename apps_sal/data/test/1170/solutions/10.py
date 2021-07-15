from math import *

def calcul(xi):
	n=int(sqrt(xi))+1
	n2=n**2
	while n2<=2*xi and n<=1000000000:
		nsm2=n2-xi
		nsm=sqrt(nsm2)
		if nsm==int(nsm):
			m=n//nsm
			if n2 - (n//m)**2 == xi:
				return n, int(m)
		n+=1
		n2=n**2
	return -1,-1

t=int(input())
for _ in range(t):
	xi=int(input())
	if xi==0:
		print("1 1")
		continue
	n,m=calcul(xi)
	if m==-1:
		print(-1)
	else:
		print(n,m)

