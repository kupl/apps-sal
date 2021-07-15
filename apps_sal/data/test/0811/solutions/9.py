a,b = list(map(int,input().split()))
poc = 0
while a >= b:
	x = a//b
	zv = a%b
	x = x*b
	poc+=x
	a = x//b+zv
print(poc+a)

