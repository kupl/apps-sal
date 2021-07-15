import sys
from math import *

def minp():
	return sys.stdin.readline().strip()

def mint():
	return int(minp())

def mints():
	return list(map(int, minp().split()))

n = mint()
c = [0]*1005
while n%2 == 0:
	n //= 2
	c[2] += 1
i = 3
while i*i <= n:
	while n%i == 0:
		n //= i
		c[i] += 1
	i += 2
m = 0
r = 1
for i in range(len(c)):
	m = max(m, c[i])
	if c[i] != 0:
		r *= i
if n != 1:
	m = max(m, 1)
	r *= n
k = 0
i = 0
while m > (1<<i):
	i += 1
mm = 1<<i
for j in range(len(c)):
	if c[j] != 0 and mm != c[j]:
		k = 1
if n != 1 and mm != 1:
	k = 1
print(r, i+k)

