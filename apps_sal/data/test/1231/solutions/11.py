a, b = map(int, input().split())

if abs(a - b) < 2 and a + b:
	print('YES')
else:
	print('NO')
