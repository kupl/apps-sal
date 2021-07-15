n = int(input())

for _ in range(n):
	a = (input())

	p = (len(a)-1)*9

	p += int(a[0]) if int(a) >= int(a[0]*len(a)) else int(a[0])-1

	print(p)

