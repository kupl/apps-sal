for _ in range(int(input())):
	n = int(input())

	ans = []

	ps = [input() for _ in range(n)]

	suf = {}

	for i in range(n):
		p = ps[i]
		s = p[1:]
		if s not in suf:
			suf[s] = [str(A) for A in range(10)]

		if p[0] in suf[s]:
			suf[s].remove(p[0])


	cnt = 0

	used = {}

	for i in range(n):
		p = ps[i]
		s = p[1:]

		if s in used and p[0] in used[s]:
			p = suf[s][-1] + s
			cnt += 1
			suf[s].pop()

		used.setdefault(s, set()).add(p[0])

		ans.append(p)

	print(cnt)
	print(*ans, sep = "\n")
