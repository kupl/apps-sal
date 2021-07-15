n=int(input())
for _ in range(n):
	a=input()[::-1]
	b=input()[::-1]
	x=b.find("1")
	print(a.find("1", x)-x)
