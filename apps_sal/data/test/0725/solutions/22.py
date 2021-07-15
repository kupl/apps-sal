import sys
sys.setrecursionlimit(20000)

from collections import Counter
from math import ceil, floor, factorial, fsum, isinf, exp, log, log10, log2, isfinite
from itertools import product

def getlist(tcast):
	return [tcast(x) for x in input().strip().split(' ')]
def getval(tcast):
	return tcast(input().strip())
def getmatrix(r, tcast):
	mat = []
	for i in range(r):
		mat.append(getlist(tcast))
	return mat

def isodd(n):
    return n & 1
def numdigits(n):
    return len(str(n)) - (1 if n < 0 else 0)
def primesupto(n):
    isp = [True] * (n + 1)
    isp[0], isp[1] = False, False
    for i, x in enumerate(isp): #for each number
        if x: #found a prime
            mults = i * i
            while mults <= n:
                isp[mults] = False
                mults += i
    return isp
def maxarrays(a, b):
    return [max(x, y) for x, y in zip(a, b)]

nr, nc = getlist(int)
mat = getmatrix(nr, str)

#print(mat)
rows = map(lambda row: set(row), mat)
#print('----')

total = set()
for r in rows:
    total.update(r)
total -= set(['B', 'W', 'G'])
#print(total)
out = len(total)


print("#Black&White" if out == 0 else "#Color")
