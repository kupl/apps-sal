s = input()
a = input().split()
for el in a:
	if el[0] == s[0] or el[1] == s[1]:
		print('YES')
		return
print('NO')

