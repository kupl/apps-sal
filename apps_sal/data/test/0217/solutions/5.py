a, b, f, k = map(int, input().split())

if (f > b or a - f > b) or (k > 1 and 2 * (a - f) > b) or (k > 2 and 2 * f > b):
	print(-1)
	return
cur = b
ans = 0
for i in range(k):
	if i & 1 == 0:
		if cur < f:
			cur = b - f
			ans += 1
		if cur >= a:
			cur -= a
		else:
			ans += 1
			cur = b - a + f
	else:
		if cur < a - f:
			cur = b - a + f
			ans += 1
		if cur >= a:
			cur -= a
		else:
			ans += 1
			cur = b - f
print(ans)
