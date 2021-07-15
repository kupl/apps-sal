from math import *


def ok(v,x,a,y,b,k,m):
	gcdd=(a*b)//gcd(a,b)
	anss=[0 for j in range(m+1)]
	idd=0

	for i in range(1,m+1):
		if(i % gcdd == 0):
			anss[i] = (v[idd] * (x+y)) // 100;
			idd+=1;
	maxmass = a; maxmastt = b; mx = x; mn = y;
	if(x > y):
		maxmass, maxmastt, mx, mn = a,b,x,y;
	else:
		maxmass, maxmastt, mx, mn = b,a,y,x;

	for i in range(1,m+1):
		if(i % maxmass == 0 and anss[i] == 0):
			anss[i] = (v[idd] * mx) // 100;
			idd+=1;
	for i in range(1,m+1):
		if(i % maxmastt == 0 and anss[i] == 0):
			anss[i] = (v[idd] * mn) // 100;
			idd+=1;
	summ = 0;
	for i in range(1, m+1):
		summ += anss[i]	
	return (summ >= k)

for _ in ' '*int(input()):
	n=int(input())
	v=[int(i) for i in input().split()]
	for i in range(10):
		v.append(0)
	x,a=[int(i) for i in input().split()]
	y,b=[int(i) for i in input().split()]
	k=int(input())
	v.sort(reverse=True)
	hi,lo=n+1,-1
	midd=(hi+lo)//2
	while(hi-lo>1):
		midd=(hi+lo)//2
		if(ok(v,x,a,y,b,k,midd)):
			hi=midd
		else:
			lo=midd
	if(ok(v,x,a,y,b,k,lo)):
		print(lo)
	elif(ok(v,x,a,y,b,k,hi)):
		print(hi)
	else:
		print(-1)

