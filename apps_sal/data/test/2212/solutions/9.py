n=int(input())
a=2
b=1
for i in range(n):
	for j in range(n):
		if j>=i and j!=n//2 and j<=n-1-i:
			print(a,end=' ')
			a=a+2
		
		elif j>=n-1-i and j!=n//2 and j<=i:
			print(a,end=' ')
			a=a+2
		else:
			print(b,end=' ')
			b=b+2
	print()

