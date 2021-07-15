import math
for _ in range(int(input())):
	n,k=list(map(int,input().split()))
	l=k//(n-1)
	r=k%(n-1)
	if r==0:
		r=-1
	print(l*n+r)



	

