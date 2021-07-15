n = int(input())
for i in range(n):
	x, y = list(map(int, input().split()))
	if x > y:
		x, y = y, x
	a = (y - x) // 5
	x += a * 5
	b = (y - x) // 2
	x += b * 2
	c = (y - x)
	print(a + b + c)

