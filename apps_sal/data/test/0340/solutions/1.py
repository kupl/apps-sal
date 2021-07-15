n = int(input())

if n == 1:
	print('1 0')
else:
	d = 2
	decomp = []
	while d * d <= n:
		cnt = 0
		while n % d == 0:
			cnt += 1
			n //= d
		if cnt > 0:
			decomp += [(d, cnt)]
		if d == 2:
			d += 1
		else:
			d += 2
	if n > 1:
		decomp += [(n, 1)]

	tar = 1
	maxExp = 0
	for e in decomp:
		tar *= e[0]
		maxExp = max(maxExp, e[1])
	
	divCnt = 0
	curExp = 1
	while curExp < maxExp:
		divCnt += 1
		curExp *= 2

	mulRequired = False
	for e in decomp:
		if e[1] != curExp:
			mulRequired = True
			break
	if mulRequired:
		divCnt += 1

	print('%s %s' % (tar, divCnt))


