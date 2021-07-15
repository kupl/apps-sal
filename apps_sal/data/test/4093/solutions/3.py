q = int(input())
for _ in range(q):
	n,m = map(int,input().split())
	if n > 2:
		print(2*m)
	else:
		if n == 1:
			print(0)
		else:
			print(m)
