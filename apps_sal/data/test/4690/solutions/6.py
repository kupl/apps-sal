a,b,c,d = map(int,input().split())

x = a*b
y = c*d

if x>y:
	print(x)
elif y>=x:
	print(y)
