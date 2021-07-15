t=int(input())
for i in range(t):
	n,k=map(int,input().split())
	if n<k:
		print(k-n)
	else:
		print((n+k)%2)
