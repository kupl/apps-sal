n = int(input())

d = n // 10
a1 = d * 10
a2 = (d + 1) * 10

if (abs(a1 - n) > abs(a2 - n)):
	print(a2)
else:
	print(a1)

