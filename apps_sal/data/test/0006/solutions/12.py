t = int(input())
for i in range(t):
	a = input().split(' ')
	n = int(a[1])
	m = 0
	eff = 0 
	for j in range(int(a[0])):
		b = input().split(' ')
		m = max(m,int(b[0]))
		eff = max(eff,int(b[0])-int(b[1]))
	n -= m
	if n > 0:
		if eff>0:
			print((n-1)//eff+2)
		else:
			print(-1)
	else: 
		print(1)
