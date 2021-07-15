from math import *
t=int(input())
for l in range(t):
	a,b,c,d,k=list(map(int,input().split()))
	val1=ceil(a/c)
	val2=ceil(b/d)
	if(val1+val2<=k):
		print(val1,val2)
	else:
		print(-1)

