s = input()
a = 0
su = 0

for i in range(len(s)):
	if s[i : i + 5] == 'heavy':
		a += 1
	elif s[i : i + 5] == 'metal':
		su += a
print(su)

