n = int(input())
if n<3: print(-1)
else:
	x=int('1'+'0'*(n-1))
	x=x+(210-x%210)
	print(x)
