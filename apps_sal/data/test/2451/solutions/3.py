n,h,a,b,k=list(map(int,input().strip().split()))
for i in range(k):
	t1,f1,t2,f2=list(map(int,input().strip().split()))
	if (t1==t2):
		print(abs(f1-f2))
		continue
	else:
		e=abs(t1-t2)
		if (f1>=a and f1<=b):
			print(e+abs(f1-f2))
		elif (f1<a):
			print(e+a-f1+abs(a-f2))
		else:
			print(e+f1-b+abs(b-f2))

