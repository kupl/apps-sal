n=int(input())
for i in range(n):
	n,k=map(int,input().split())
	a=list(map(int,input().split()))
	if max(a)-min(a)>2*k:
		print(-1)
	else:
		print(min(a)+k)
