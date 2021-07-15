a = input()
for i in range(len(a)):
	if a[i] != a[len(a) - i - 1] or a[i] not in ('A','H','I','M','O','T','U','V','W','X','Y'):
		print("NO")
		return
print("YES")
