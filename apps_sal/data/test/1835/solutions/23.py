q = int(input())
for fwefe in range(q):
	n = int(input())
	j = 0
	z = 0
	par = []
	npar = []
	for i in range(n):
		s = input()
		je = s.count('1')
		ze = s.count('0')
		j += je
		z += ze
		if len(s) % 2 == 0:
			par.append(len(s))
		else:
			npar.append(len(s))
	par.sort()
	wyn = 0
	for i in par:
		if j < 0 or z < 0:
			break
		kz = 0
		while z - kz > j - (i - kz) and z - kz >= 0 and kz <= i:
			kz += 2
		z -= kz
		j -= (i-kz)
		wyn += 1
		if j < 0 or z < 0:
			wyn -= 1
	wyn += len(npar)
	print(wyn)
			
	

