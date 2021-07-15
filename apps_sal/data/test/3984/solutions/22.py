import math
from decimal import Decimal
import heapq
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
 
 
def lol(lst,k):
	k=k%len(lst)
	ret=[0]*len(lst)
	for i in range(len(lst)):
		if i+k<len(lst) and i+k>=0:
			ret[i]=lst[i+k]
		if i+k>=len(lst):
			ret[i]=lst[i+k-len(lst)]
		if i+k<0:
			ret[i]=lst[i+k+len(lst)]
	return(ret)
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
def Factor(n):
	Ans = []
	d = 2
	while d * d <= n:
		if n % d == 0:
			Ans.append(d)
			n //= d
		else:
			d += 1
	if n > 1:
		Ans.append(n)
	return Ans


s = input()
a1 = 'Mike'
a2 = 'Ann'
if len(s) == 1:
	print(a1)
	return
print(a1)
tc = s[0]
pre = []
n = len(s)
for i in range(1, n):
	d = min(s[i], tc)
	pre.append(d)
	tc = d
for i in range(1, n):
	if pre[i - 1] < s[i]:
		print(a2)
	else:
		print(a1)

