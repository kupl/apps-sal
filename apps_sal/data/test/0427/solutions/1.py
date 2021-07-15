c1, c2, x, y = list(map(int, input().split()))
l, r = 0, 1 << 179
while r - l > 1:
	m = (l + r) >> 1
	if (m - m // x >= c1) and (m - m // y - max(0, c1 - m // y + m // x // y) >= c2):
		r = m
	else:
		l = m
print(r)

