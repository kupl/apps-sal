for i in range(int(input())):
	b, p, f = list(map(int, input().split()))
	h, c = list(map(int, input().split()))
	mc = 0
	if h > c:
		mc += h * min(b // 2, p)
		b, p = b - 2 * min(b // 2, p), p - min(b // 2, p)
		mc += c * min(b // 2, f)
	else:
		mc += c * min(b // 2, f)
		b, f = b - 2 * min(b // 2, f), p - min(b // 2, f)
		mc += h * min(b // 2, p)
	print(mc)

