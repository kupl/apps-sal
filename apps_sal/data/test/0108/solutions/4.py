s = list(input())

a = "abcdefghijklmnopqrstuvwxyz"

i = 0
j = 0

while i < len(a) and j < len(s):
	if s[j] <= a[i]:
		s[j] = a[i]
		i += 1
	j += 1

if i == len(a):
	print("".join(s))
else:
	print(-1)

