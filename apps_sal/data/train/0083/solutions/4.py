for _ in range(int(input())):
	x, y, a, b = list(map(int, input().split()))
	
	t = (y - x) / (a + b)
	tz = (y - x) // (a + b)

	if t != tz:
		print(-1)
	else:
		print(tz)

