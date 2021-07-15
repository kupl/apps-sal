t=int(input())
for l in range(t):
	n=int(input())
	arr=list(map(int,input().split()))
	arr.sort()
	a=arr[-2]
	print(min(a-1,n-2))

