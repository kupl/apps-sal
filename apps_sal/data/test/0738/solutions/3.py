def cnt(x) :
	return x * (x + 1) // 2
t = 1
while t > 0:
	t -= 1
	a, b, c, d = map(int, input().split())
	ans = 0
	for x in range(a, b + 1) :
		l, r = x + b, x + c
		ans += cnt(min(r, d) - c) - cnt(max(min(l - 1, d) - c, 0))
		ans += max(0, r - max(d, l - 1)) * (d - c + 1)
	print(ans)
