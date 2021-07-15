input()
s = input()
c1 = c2 = 0
for i in s:
	if i == 'A':
		c1 += 1
	else:
		c2 += 1

if c1 > c2:
	print('Anton')
elif c1 < c2:
	print('Danik')
else:
	print('Friendship')

