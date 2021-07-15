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

m=10000019
def binomialCoefficient(n , k):
	if (k > n - k):
		k = (n - k)%m
	res = 1
	for i in range(k):
		res = (res * (n - i))%m
		res = (res * modInverse((i + 1),m))%m
	return res


def num():
	return map(int , input().split())


def nu():
	return int(input())


def find_gcd(x , y):
	while (y):
		x , y = y , x % y
	return x


n,m=num()
a=[0]*(m)
for ii in range(n):
	l,r=num()
	for i in range(l-1,r):
		a[i]=1
c=0
ll=[]
for i in range(m):
	if(a[i]==0):
		c+=1
		ll.append(i+1)
print(c)
print(*ll,sep=" ")
