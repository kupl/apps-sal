import sys

def pro():
	return sys.stdin.readline().strip()

def rop():
	return map(int, pro().split())

def a_b_b(a, b):
	return a > b

def a_br_b(a, b):
	return a >= b

def a_m_b(a, b):
	return a < b

def a_mr_b(a, b):
	return a <= b

def ry(a, c, t):
	q = len(a)
	x = [(t, -1)]
	r = [0] * q
	
	for i in range(len(a)):
		v = a[i]
		
		while c(v, x[-1][0]):
			x.pop()
		r[i] = x[-1][1]
		x.append((v, i))
		
	return r

def tyr(a):
	q = len(a)
	r = [0] * q
	
	for i in range(q):
		r[q - i - 1] = q - a[i] - 1
		
	return r

def main():
	s = int(pro())
	a = list(rop())
	z = a[::-1]
	o = 10 ** 9
	r = 0
	
	m = ry(a, a_b_b, o)
	n = tyr(ry(z, a_br_b, o))
	b = ry(a, a_m_b, -o)
	v = tyr(ry(z, a_mr_b, -o))
	
	for i in range(s):
		r += a[i] * ((i - m[i]) * (n[i] - i) - (i - b[i]) * (v[i] - i))
		
	print(r)
main()
