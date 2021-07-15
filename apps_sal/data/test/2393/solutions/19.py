n = int(input())

for _ in range(n):
	s = input()

	ans = []
	i = 0
	while i < len(s):
		if s[i:i+3] == 'one':
			ans.append(i + 1)
			i += 3
		elif s[i:i+3] == 'two':
			if s[i:i+5] == 'twone':
				ans.append(i + 2)
				i += 5
			else:
				ans.append(i + 1)
				i += 3
		else:
			i += 1

	print(len(ans))
	print(' '.join(list(map(lambda x: str(x+1), ans))))
