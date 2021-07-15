import math

for _ in range(int(input())):
	s = input()
	n = len(s)
	ans = 0
	lg = int(math.log2(n)) + 1
	npfx = 0
	for i in range(n):
		if s[i] == '0':
			npfx += 1
			continue
		ans += 1
		cv = 1
		ln = 1
		for j in range(i + 1, min(i + lg + 1, n)):
			ln += 1
			cv *= 2
			cv += s[j] == '1'
			ans += (ln <= cv) and (ln + npfx >= cv)
		npfx = 0
	print(ans)

