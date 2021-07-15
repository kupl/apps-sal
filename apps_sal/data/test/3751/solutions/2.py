s = input()
i = 0
f = True
while len(s):
	if s[0] != chr(97 + i):
		f = False
		break
	s = s.replace(chr(97 + i), '')
	i += 1
print('YES' if f else 'NO')
