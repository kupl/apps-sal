

	

def ff(p, q, pp):
	npp = []
	for r in pp:
		if (p[1] - r[1]) * (p[0] - q[0]) != (p[1] - q[1]) * (p[0] - r[0]):
			npp.append(r)
	
	if len(npp) <= 2:
		return True
		
	a = npp[0]
	b = npp[1]
	for c in npp:
		if (a[1] - c[1]) * (a[0] - b[0]) != (a[1] - b[1]) * (a[0] - c[0]):
			return False
	
	return True
	
	
	
	

n = int(input())
if n <= 4:
	print('YES')
	

else:
	pp = []
	for _ in range(n):
		a, b = [int(x) for x in input().split()]
		pp.append((a,b))

	if ff(pp[0], pp[1],pp) or ff(pp[1], pp[2],pp) or ff(pp[0], pp[2],pp):
		print('YES')
	else:
		print('NO')
	
	

