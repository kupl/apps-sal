s = input()
n = len(s)

v = {'a', 'o', 'u', 'i', 'e'}

for i in range(n-1):
	if s[i] not in v:
		if s[i] != 'n':
			if s[i+1] not in v:
				print('NO')
				return
		
if(s[n-1] not in v) and (s[n-1] != 'n'):
	print('NO')
else:
	print('YES')
