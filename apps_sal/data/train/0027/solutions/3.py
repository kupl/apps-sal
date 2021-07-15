for _ in range(int(input())):
	d = dict()
	N = int(input())
	a = list(map(int, input().split()))
	for i in range(N):
		c = 0
		tmp = a[i]
		while tmp % 2 != 1:
			tmp = tmp // 2
			c += 1
		if tmp in d:
			d[tmp] = max(d[tmp], c)
		else:
			d[tmp] = c
	res = 0
	for i in list(d.keys()):
		res += d[i]
	print(res)


