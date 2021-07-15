q = int(input())
for rere in range(q):
	a, b = map(int,input().split())
	d = abs(b-a)
	i = 0
	while i*(i+1)//2 < d:
		i += 1
	if  (d%2) == ((i*(i+1)//2)%2):
		print(i)
	else:
		a = ((i*(i+1)//2)%2)
		while ((i*(i+1)//2)%2) == a:
			i += 1
		print(i)
