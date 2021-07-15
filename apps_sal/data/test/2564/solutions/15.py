n = int(input())
for i in range(n):
	a, b, n = list(map(int, input().split()))
	t = 0
	while a <= n and b <= n:
		if a <= b:
			a += b
		else:
			b += a
		t += 1
	print(t)
