q=int(input())

for i in range(q):
	n,m,k=list(map(int,input().split()))

	if n>k or m>k:
		print(-1)

	else:
		if n%2==0 and m%2==0:
			if k%2==0:
				print(k)
			else:
				print(k-2)

		elif (n%2==0 and m%2==1) or (n%2==1 and m%2==0):
			print(k-1)

		elif n%2==1 and m%2==1:
			if k%2==0:
				print(k-2)
			else:
				print(k)

