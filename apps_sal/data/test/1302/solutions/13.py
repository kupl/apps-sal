n, k = [int(x) for x in input().split()]

if k==n:
	print(-1)
elif n==1 and k==0:
	print(1)
else:
	storti = n-k
	for i in range(2, n-k+1):
		print(i, end=' ')
	print(1, end=' ')
	for i in range(n-k+1, n+1):
		print(i, end=' ')

