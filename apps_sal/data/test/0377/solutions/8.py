a, b = map(int, input().split())

if b > a / 2:
	print(a - b)
elif b < 1:
	print(1)
else:
	print(b)
