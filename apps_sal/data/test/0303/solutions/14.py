x1, y1, x2, y2 = list(map(int, input().split()))
x, y = list(map(int, input().split()))
x0, y0 = x2 - x1, y2 - y1
x0, y0 = abs(x0), abs(y0)
for a in range(- 2 * 10 ** 5, 2 * 10 ** 5 + 1):
	if x0 % x == 0:
		b = x0 // x - a
		if a * y - b * y == y0:
			print('YES')
			return
print('NO')

