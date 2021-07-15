for i in range(8):
	s = input()
	for a, b in zip(s, (s + s[0])[1: ]):
		if a == b:
			print('NO')
			return
print('YES')

