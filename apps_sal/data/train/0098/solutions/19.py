for _ in range(int(input())):
	c, m, a = map(int, input().split())
	print(min(c, m, (c + m + a) // 3))
