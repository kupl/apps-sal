t = int(input())
for i in range(t):
	n = int(input())
	n1 = n
	q = 1
	while n1 != 0:
		n1 = n1 // 2
		q *= 2
	q = q // 2
	print(n * (n + 1) // 2 - 2 * (2 * q - 1))
