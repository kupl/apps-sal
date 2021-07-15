n, s = int(input()), input()
for i in range(n - 1):
	if ord(s[i]) > ord(s[i + 1]):
		print ("YES")
		print (i + 1, i + 2, sep = ' ')
		return
print ("NO")
