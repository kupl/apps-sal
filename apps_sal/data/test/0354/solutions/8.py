vowels = ['a','e','i','o','u']
s = input()
t = input()
if len(s)!= len(t):
	print("No")
	return
else:
	for i in range(len(s)):
		if s[i] in vowels and t[i] not in vowels:
			print("No")
			return
		elif s[i] not in vowels and t[i] in vowels:
			print("No")
			return
	print("Yes")
