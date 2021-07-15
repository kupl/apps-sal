a, b, c = map(int, input().split())

def sumd(x):
	s = 0
	while x > 0:
		s += x % 10
		x = x // 10
	return s
sol = []
for s in range(1, 82):
	x = b*pow(s, a) + c
	if x > 0 and x < 1000000000 and sumd(x) == s:
		sol.append(x)
print(len(sol))
for el in sorted(sol):
	print(el, end=' ')

