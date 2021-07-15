for _ in range(int(input())):
	n=int(input())
	ans=0
	for i in range(1,10):
		f=0
		for j in range(1,5):
			k=int(str(i)*j)
			ans+=len(str(k))
			if k==n:f=1;break
		if f:break
	print(ans)
