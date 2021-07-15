            

n,a,b = list(map(int,input().split()))



def check(x):
	A = a
	B = b
	if A >= x and B >= x:
		A -= x
		B -= x
	else:
		return False
	for i in range(n-2):
		if A >= x:
			A -= x
		elif B >= x:
			B -= x
		else:
			return False
	return True

l = 0 
r = a+b

while l + 1 < r:
	m = (l+r) // 2
	if check(m):
		l = m
	else:
		r = m
print(l)

