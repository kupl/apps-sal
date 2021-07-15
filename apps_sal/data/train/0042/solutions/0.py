LOG = 20

def solve(s):
	n = len(s)
	res = 0
	z = 0
	for t in range(0, n):
		if s[t] == '0':
			z += 1
			continue
		for l in range(1, min(LOG, n - t + 1)):
			x = int(s[t:t+l], 2)
			# print(l, t, x, l + z)
			if l + z >= x:
				res += 1

#			print(t, l, x, res, z)
		z = 0
	return res


t = int(input())
while t > 0:
	t -= 1
	s = input()
	print(solve(s))
