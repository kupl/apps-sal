import math as ma
from decimal import Decimal as dec


def li():
	return list(map(int , input().split()))


# https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
def modInverse(a , m):
	m0 = m
	y = 0
	x = 1
	if (m == 1):
		return 0
	while (a > 1):
		q = a // m
		t = m
		m = a % m
		a = t
		t = y
		y = x - q * y
		x = t
	if (x < 0):
		x = x + m0
	return x


m = 10000019


def binomialCoefficient(n , k):
	if (k > n - k):
		k = (n - k) % m
	res = 1
	for i in range(k):
		res = (res * (n - i)) % m
		res = (res * modInverse((i + 1) , m)) % m
	return res


def num():
	return map(int , input().split())


def nu():
	return int(input())


def find_gcd(x , y):
	while (y):
		x , y = y , x % y
	return x


n , m = num()
a = [0] * n
b = [0] * n
for i in range(n):
	x = input()
	a[i] = [0] * m
	b[i] = [0] * m
	for j in range(m):
		if (x[j] == "*"):
			a[i][j] = 1
pp=[]
for i in range(n):
	for j in range(m):
		u = 0
		d = 0
		l = 0
		r = 0
		if (a[i][j] == 1):
			for k in range(i - 1 , -1 , -1):
				if (a[k][j] == 1):
					u += 1
				else:
					break
			for k in range(i + 1 , n):
				if (a[k][j] == 1):
					d += 1
				else:
					break
			for k in range(j - 1 , -1 , -1):
				if (a[i][k] == 1):
					l += 1
				else:
					break
			for k in range(j + 1 , m):
				if (a[i][k] == 1):
					r += 1
				else:
					break
			zz = min(u , d , l , r)
			#print(i,j,zz)
			if(zz==0):
				continue
			pp.append((i+1,j+1,zz))
			b[i][j] = 1
			c=0
			for k in range(i - 1 , -1 , -1):
				b[k][j]=1
				c+=1
				if(c==zz):
					break
			c=0
			for k in range(i + 1 , n):
				b[k][j] = 1
				c += 1
				if (c == zz):
					break
			c=0
			for k in range(j - 1 , -1 , -1):
				b[i][k]=1
				c += 1
				if (c == zz):
					break
			c=0
			for k in range(j + 1 , m):
				b[i][k] = 1
				c+=1
				if(c==zz):
					break
fl=True
for i in range(n):
	for j in range(m):
		if(a[i][j]==1 and b[i][j]==0):
			fl=False
			break
if(fl):
	print(len(pp))
	for i in range(len(pp)):
		print(pp[i][0],pp[i][1],pp[i][2])
else:
	print(-1)
