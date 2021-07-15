n = int(input())

l = []
for i in range(n):
	s = input().rstrip().lstrip()
	l.append(s)

for i in range(n):
	s = l[i]
	ind = s.find('OO')
	if ind != -1:
		s = list(s)
		s[ind] = '+'
		s[ind + 1] = '+'
		l[i] = ''.join(s)
		print('YES')
		print('\n'.join(l))
		return
print('NO')

