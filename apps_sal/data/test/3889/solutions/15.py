import math as ma
from decimal import Decimal as dec
from itertools import permutations


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


def num():
	return map(int , input().split())


def nu():
	return int(input())


def find_gcd(x , y):
	while (y):
		x , y = y , x % y
	return x

n=nu()
s=input()
f=[0]*26
for i in range(n):
	x=ord(s[i])-97
	f[x]+=1
fl=False
for i in range(26):
	if(f[i]>=2):
		fl=True
if(n==1):
	fl=True
if(fl==True):
	print("Yes")
else:
	print("No")
