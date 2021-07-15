import copy
import fractions
import itertools
import numbers
import string
import sys

###

def to_basex(num, x):
	while num > 0:
		yield num % x
		num //= x

def from_basex(it, x):
	ret = 0
	p = 1
	for d in it:
		ret += d*p
		p *= x
	return ret

###

def core():
	n, v = [int(x) for x in input().split()]
	
	ans = min(v, n-1)
	
	if n-v > 1:
		ans += (2 + n-v)*(n-v - 2 + 1)//2
	
	print(ans)


core()



















