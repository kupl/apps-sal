n, k = map(int, input().split())

l = [0, 0, 2 * n, 0, n]

inp = sorted(map(int, input().split()), reverse = True)

for i in range(k):
	if inp[i] > 1 and inp[i] & 1:
		inp[i] -= 1
		inp.append(1)

for a in inp:
	if a == 1:
		if l[1]:
			l[1] -= 1
			a = 0
		elif l[2]:
			l[2] -= 1
			a = 0
		elif l[4]:
			l[4] -= 1
			l[2] += 1
			a = 0
	else:	
		while a > 2 and l[4]:
			a -= 4
			l[4] -= 1
		while a and l[2]:
			a -= 2
			l[2] -= 1
		while a and l[4]:
			a -= 2
			l[4] -= 1
			l[1] += 1
		while a and l[1]:
			a -= 1
			l[1] -= 1

	if a:
		print('NO')
		return

print('YES')
