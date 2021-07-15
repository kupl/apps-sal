s = input().strip()


iter = 'a'
for i in range(len(s)):
	if ord(s[i]) < ord(iter):
		continue
	elif ord(s[i]) == ord(iter):
		iter = chr(ord(iter) + 1)
	else:
		print('NO')
		return
		
print('YES')


