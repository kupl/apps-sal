import math
for _ in range(int(input())):
	n=int(input())
	li=list(map(int,input().split()))
	a=0
	b=0
	l=0
	r=n-1
	p=0
	q=0
	while(l<=r):
		if q%2==0:
			su=0
			for i in range(l,r+1):
				l+=1
				su+=li[i]
				a+=li[i]
				if (su>p):
					p=su
					break
		else:
			su=0
			for i in range(r,l-1,-1):
				r-=1
				su+=li[i]
				b+=li[i]
				if (su>p):
					p=su
					break
		q+=1
	print(q,a,b)






	

