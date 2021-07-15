n = int(input())
s = list(input())
l, r = s.count('('), s.count(')')
for i in range(n):
	if s[i] == '?':
		if l + l < n:
			s[i] = '('
			l += 1
		else:
			s[i] = ')'
cnt = 0
for i in range(n):
	cnt += 1 if s[i] == '(' else -1
	if cnt < 1 and i < n - 1:
		print(':(')
		return
	elif cnt != 0 and i == n - 1:
		print(':(')
		return
print(''.join(s))
