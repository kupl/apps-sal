a, b, c = [int(x) for x in input().split()]
x, y, z = [int(x) for x in input().split()]

i = (a - x) // 2 if a > x else 0
j = (b - y) // 2 if b > y else 0
k = (c - z) // 2 if c > z else 0

if max(x - a, 0) + max(y - b, 0) + max(z - c, 0) <= i + j + k:
	print('Yes')
else:
	print('No')

