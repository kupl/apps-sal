n = int(input())

for _ in range(n):
	s1 = input()
	s2 = input()

	d1 = []
	d2 = []

	actual = s1[0]
	cont = 1

	for c in s1[1:]:
		if c != actual:
			d1.append((actual, cont))
			actual = c
			cont = 1
		else:
			cont += 1
	d1.append((actual, cont))

	actual = s2[0]
	cont = 1

	for c in s2[1:]:
		if c != actual:
			d2.append((actual, cont))
			actual = c
			cont = 1
		else:
			cont += 1
	d2.append((actual, cont))

	if len(d1) != len(d2):
		print("NO")
	else:
		for a, b in zip(d1, d2):
			if a[0] != b[0] or a[1] > b[1]:
				print("NO")
				break
		else:
			print("YES")

