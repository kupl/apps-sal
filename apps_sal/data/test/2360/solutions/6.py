t = int(input())
for _ in range(t):
	n = int(input())
	d = []
	for i in range(n):
		d.append(list(map(int, input().split())) + [i])
	d.sort(key = lambda x: x[1])
	d.sort(key = lambda x: x[2])
	d.sort(key = lambda x: x[0])
	res = [[d[0][0], d[0][2]]]
	c = d[0][0]
	i = 0
	while i < len(d):
		while i < len(d) and d[i][1] < c:
			res.append([0, d[i][2]])
			i += 1
		if i < len(d):
			c = max(c + 1, d[i][0] + 1)
			res.append([c - 1, d[i][2]])
		i += 1
	res.pop(0)
	res.sort(key = lambda x: x[1])
	z = [res[i][0] for i in range(len(res))]
	print(*z)

