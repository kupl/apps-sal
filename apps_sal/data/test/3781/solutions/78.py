T=int(input())
while(T):
	T=T-1
	n=int(input())
	a=list(map(int,input().split()))
	a.sort()
	if(len(a)&1):
		print("Second")
	else:
		f=0
		for i in range(1,len(a),2):
			if(a[i]!=a[i-1]):
				f=1
		if(f):
			print("First")
		else:
			print("Second")

