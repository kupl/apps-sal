# a1 <=> a2: 
# cos, cos^2 (0-90), val (0-360)

V, N, X, Y, L = list(range(5))

def sec(x, y):
	if x>0 and y>=0:
		s = 1
	elif x<=0 and y>0:
		s = 2
	elif x<0 and y<=0:
		s = 3
	else:
		s = 4
	return s

def val(a, b, s):
	# a/b+c = (a+bc)/b
	if s == 1:
		# 1 - a/b
		a = -a + b
	elif s == 2:
		# 2 + a/b - 1 = a/b + 1
		a = a + b
	elif s == 3:
		# 3 - a/b
		a = -a + 3*b
	else:
		# 4 + a/b - 1 = a/b + 3
		a = a + 3*b
	return a/b
	
def vec(n, x, y):
	# cos = x/sqrt(xx+yy)
	a = x*x
	b = l = x*x + y*y
	s = sec(x, y)
	v = val(a, b, s)
	return (v, n, x, y, l)
	
def ang(v1, v2):
	# cos = (v1,v2) / |v1||v2|
	v = v1[X] * v2[X] + v1[Y] * v2[Y]
	s = 1 if v > 0 else 2
	a = v * v
	b = v1[L] * v2[L]
	return val(a, b, s)
	
def quiz():		
	n = int(input())
	a = []
	for i in range(n):
		x, y = list(map(int, input().split()))
		a.append(vec(i+1,x,y))

	a.sort(key=lambda x: x[V])
	
	imin, vmin = 0, 3
	for i in range(0, n):
		v = ang(a[i-1], a[i])
		if v < vmin:
			vmin = v
			imin = i
	
	print(a[imin-1][N], a[imin][N])
	
quiz()

