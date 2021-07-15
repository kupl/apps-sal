import math
from decimal import Decimal
def na():
	n = int(input())
	b = [int(x) for x in input().split()]
	return n,b
 
 
def nab():
	n = int(input())
	b = [int(x) for x in input().split()]
	c = [int(x) for x in input().split()]
	return n,b,c
 
 
def dv():
	n, m = list(map(int, input().split()))
	return n,m
 
 
def dva():
	n, m = list(map(int, input().split()))
	a = [int(x) for x in input().split()]
	b = [int(x) for x in input().split()]
	return n,m,b
 
 
def eratosthenes(n): 
	sieve = list(range(n + 1))
	for i in sieve:
		if i > 1:
			for j in range(i + i, len(sieve), i):
				sieve[j] = 0
	return sorted(set(sieve))
 
 
 
def nm():
	n = int(input())
	b = [int(x) for x in input().split()]
	m = int(input())
	c = [int(x) for x in input().split()]
	return n,b,m,c
 
 
def dvs():
	n = int(input())
	m = int(input())
	return n, m
 

x, y ,z = list(map(int, input().split()))
s1 = x // z + y // z
rz = z - x % z
rz2 = z - y % z
x1 = x + rz
y1 = y - rz
x2 = x - rz2
y2 = y + rz2
s2 = x1 // z + y1 // z
s3 = x2 // z + y2 // z
xx = max(s1, s2, s3)
if xx == s1:
	print(xx, 0)
elif xx == s2 and s2 != s3:
	print(s2, rz)
elif xx == s2 == s3:
	print(s2, min(rz, rz2))
elif xx == s3:
	print(s3, rz2)

