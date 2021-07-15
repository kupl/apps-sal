s = input()
t = input()
vow = 'aeoui'
if len(s) != len(t):
	print("No")
else:
	for i in range(len(s)):
		if (s[i] in vow) != (t[i] in vow):
			print("No")
			break
	else:
		print("Yes")

