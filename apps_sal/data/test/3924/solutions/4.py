import math as ma
import sys
from decimal import Decimal as dec
from itertools import permutations

def li():
	return list(map(int , input().split()))

def num():
	return map(int , input().split())

def nu():
	return int(input())

def find_gcd(x , y):
	while (y):
		x , y = y , x % y
	return x

n,k=num()
a=li()
z=0
x=0
for i in range(n):
	if(z%k==0):
		x+=int(ma.ceil(z/k))+a[i]//k
		z = a[i] % k
	else:
		cp=z%k
		zz=a[i]-(k-cp)
		if(zz<0):
			zz=0
		x+=int(ma.ceil(z/k))+zz//k
		z=zz%k
if(z>0):
	x+=1
print(x)
