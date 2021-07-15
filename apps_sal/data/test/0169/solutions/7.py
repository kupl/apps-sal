n = int(input())
a = int(input())
b = int(input())
c = int(input())


if a > (b - c):
	x = ((n - b) // (b - c))
	if x < 0:
		x = n // a
		print(x)
	else:
		n -= (x + 1) * (b - c)
		x += 1
		x += n // a
		print(x)
else:
	x = (n // a)
	print(x)

