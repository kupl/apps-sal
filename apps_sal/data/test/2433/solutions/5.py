T = int(input())

for t in range(T):
	b, p, f = list(map(int, input().split()))
	h, c = list(map(int, input().split()))

	ans = 0

	if h > c:
		n = min(b // 2, p)

		ans += n * h

		b -= n * 2

		n = min(b // 2, f)

		ans += n * c

	else:
		n = min(b // 2, f)

		ans += n * c

		b -= n * 2

		n = min(b // 2, p)

		ans += n * h

	print(ans)

