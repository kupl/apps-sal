n, m = list(map(int, input().split()))
inp = tuple(([] for _ in range(m)))
for __ in range(n):
	s, r = list(map(int, input().split()))
	inp[s - 1].append(r)
for rs in inp:
	rs.sort(reverse=True)
res = 0
inp1 = list(map(iter, inp))
curs = [0] * m
for ___ in range(n):
	cur = 0
	i = 0
	while i < m:
		try:
			curs[i] += next(inp1[i])
			if curs[i] < 0:
				raise StopIteration
			cur += curs[i]
			i += 1
		except StopIteration:
			m -= 1
			try:
				inp1[i] = inp1.pop()
			except IndexError:
				pass
			try:
				curs[i] = curs.pop()
			except IndexError:
				pass
	res = max(res, cur)
print(res)

