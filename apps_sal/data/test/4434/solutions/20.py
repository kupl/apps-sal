t=int(input())
for _ in range(t):
	n=int(input())
	ans=0
	for i in range(1,n//2+1):
		ans+=8*i*i
	print(ans)
