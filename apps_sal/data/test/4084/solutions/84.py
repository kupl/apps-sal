n, a, b = [int(i) for i in input().split()]

if a + b == 0:
	print(0)
	return

division = n // (a + b)
surplus = n % (a + b)
print(division * a + min(a, surplus))
