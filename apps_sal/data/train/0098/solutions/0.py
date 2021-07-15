q = int(input())
for _ in range(q):
	c, m, x = list(map(int, input().split()))
	print(min([c, m, (c + m + x) // 3]))
