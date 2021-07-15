for _ in range(int(input())):
	l=sorted(list(map(int,input().split())))
	print(min(l[0]+l[1],sum(l)//2))
