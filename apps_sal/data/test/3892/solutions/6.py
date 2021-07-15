def __starting_point():
	from sys import stdin
	n, m = list(map(int, stdin.readline().split()))
	c = {}
	for _ in range(m):
		a, b = list(map(int, stdin.readline().split()))
		if (a-1) not in c.keys():
			c[a-1] = []
		x = b-a + (n if b<a else 0)
		c[a-1].append(x)

	for k, l in c.items():
		c[k] = min(l) + ((len(l)-1)*n)

	out_ = []
	for x in range(n):
		res = 0
		for y, v in c.items():
			s = y-x + (n if y<x else 0)
			res = max(res, v+s)
		out_.append(res)

	print(*out_)
__starting_point()
