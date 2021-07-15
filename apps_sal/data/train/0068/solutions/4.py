for _ in range(int(input())):
	n = int(input())

	s = list(input())

	groups = []
	last = ''
	cnt = 0
	for c in s:
		if c != last:
			if cnt: groups.append(cnt)
			cnt = 1
		else:
			cnt += 1
		last = c

	if cnt: groups.append(cnt)

	m = len(groups)
	i = 0
	j = 0

	ops = 0
	while i < m:
		ops += 1

		while j < i or (j < m and groups[j] == 1): j += 1

		if j < m: groups[j] -= 1
		else: i += 1
		i += 1

	print(ops)



