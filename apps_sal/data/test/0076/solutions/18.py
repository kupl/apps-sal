n, m, a, b = list(map(int, input().split()))

if n % m == 0:
	print(0)
else:
	t = n // m
	t *= m
	print(min(a * (t + m - n), b * (n - t)))

