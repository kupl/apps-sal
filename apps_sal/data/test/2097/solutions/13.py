for _ in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	ans=0
	for i in range(n):
		if l[i]==0:
			l[i]=1
			ans+=1
	if sum(l)==0:
		ans+=1
	print(ans)

