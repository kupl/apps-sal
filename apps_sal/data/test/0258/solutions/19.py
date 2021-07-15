n = int(input())
a, b1, b2 = [], [], []

for i, j in enumerate(input()):
	if j == '?':
		if i < n // 2:
			b1.append(i)
		else:
			b2.append(i)
		a.append(0)
	else:
		a.append(int(j))


s1 = sum(a[:n // 2])
s2 = sum(a[n // 2:])


print('Bicarp' if s1 + 9 * (len(b1) + 1) // 2 == s2 + 9 * (len(b2) + 1) // 2 else 'Monocarp')
