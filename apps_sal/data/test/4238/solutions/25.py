s = input()

sum = 0
for c in s:
	sum += ord(c) - ord('0')

if sum%9 == 0:
	print("Yes")
else:
	print("No")

