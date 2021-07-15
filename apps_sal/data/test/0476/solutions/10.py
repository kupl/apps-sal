import sys

n = input()
for i in range(len(n)):
	if n[i] != '1' and n[i] != '4':
		print("NO")
		return
while len(n) > 0:
	s = n[0:3]
	if s == "144":
		n = n[3:]
	elif s[0:2] == "14":
		n = n[2:]
	elif s[0] == "1":
		n = n[1:]
	else:
		print("NO")
		return
print("YES")

