for _ in range(int(input())):
	n=int(input())
	if n<=1000005:
		l=[0,1]
		for k in range(n-1,0,-1):
			a=n//k
			if a>l[-1]:
				l.append(a)
		print(len(l))
		print(*l)
	else:
		l=[x for x in range(1001)]
		for k in range(1000000,0,-1):
			a=n//k
			if a>l[-1]:
				l.append(a)
		print(len(l))
		print(*l)
