for _ in range(int(input())):
	a,b=map(int, input().split())
	a,b=min(a,b),max(a,b)
	if(a*2>=b):
		print((a+b)//3)
	else:
		print(a)
