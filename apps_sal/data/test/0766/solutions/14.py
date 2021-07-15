s = dict()
for symb in list(input()):
	s[symb] = s.get(symb, 0) + 1
cnt = 0
c = []
for i in s.values():
	c.append(i)
	cnt += 1
if cnt == 4:
	print('Yes')
elif cnt == 3:
	if c[0] > 1 or c[1] > 1 or c[2] > 1:
		print('Yes')
	else:
		print('No')
elif cnt == 2:
	if c[0] > 1 and c[1] > 1:
		print('Yes')
	else:
		print('No')
else:
	print('No')
