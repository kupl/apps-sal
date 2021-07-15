x, y, a, b = [int(x) for x in input().split()]
l = []
for i in range(a, x + 1):
	for j in range(b, y + 1):
		if j < i:
			l.append(str(i) + ' ' + str(j))
print(len(l))
print('\n'.join(l))

