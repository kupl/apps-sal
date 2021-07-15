def ternary(n):
	while n:
		if n%3==2:
			return 0
		n//=3
	return 1
for _ in range(int(input())):
	n = int(input())
	if ternary(n):
		print(n)
	else:
		while ternary(n)!=1:
			n+=1
		print(n)
	

