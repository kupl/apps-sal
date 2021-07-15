def div23(a):
	while (a % 2 == 0):
		a //= 2
	while (a % 3 == 0):
		a //= 3
	return a

n = int(input())
s = [int(i) for i in input().split(' ')]
a = div23(s[0])
i = 1
while i < len(s):
	if (a != div23(s[i])):
		break
	i += 1

if i == len(s):
	print("Yes")
else:
	print("No")

