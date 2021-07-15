
# c a _ c
T = int(input())

for t in range(1, T + 1):
	# print('Case #' + str(t) + ': ', end = '')
	flag = True
	s = input()
	for i in range(len(s)):
		if s[i] == '?':
			for j in ['a', 'b', 'c']:
				if (i + 1 >= len(s) or j != s[i + 1]) and (i - 1 < 0 or j != s[i - 1]):
					s = s[:i] + j + s[i + 1:]
					break
		if (i + 1 < len(s) and s[i] == s[i + 1]) or (i - 1 >= 0 and s[i] == s[i - 1]):
			# print(i, s[i])
			flag = False
			break

	if flag:
		print(s)
	else:
		print(-1)
