t = int(input())

for _ in range(t):
	n = int(input())
	s = set.union({0}, *({i, n//i} for i in range(1, int(n**.5)+1)))
	print(len(s))
	for v in sorted(s):
		print(v, end=" ")
	print()
