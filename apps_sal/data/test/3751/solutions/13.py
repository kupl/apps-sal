s = input()

current = 97

for i in s:
	if current < ord(i):
		print("NO")
		break
	elif current == ord(i):
		current += 1
else:
	print("YES")
