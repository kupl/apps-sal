import math

def nummin(f):
	c = 0
	m = 99999999999
	for n in f:
		if n < m:
			m = n
			c = 1
		elif n == m:
			c += 1
	return m, c

def nummax(f):
	c = 0
	m = -1
	for n in f:
		if n > m:
			m = n
			c = 1
		elif n == m:
			c += 1
	return m, c


numflowers = int(input())

flowers = list(map(int, input().split()))

minvalue, mincount = nummin(flowers)

maxvalue, maxcount = nummax(flowers)

diff = maxvalue - minvalue

perms = 0
if minvalue == maxvalue:
	for i in range(1, mincount):
		perms += i
else:
	perms = mincount * maxcount

print("{} {}".format(diff, perms))

