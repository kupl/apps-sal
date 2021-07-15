import io, sys, atexit, os


import math as ma
from decimal import Decimal as dec
from itertools import permutations


def li ():
	return list (map (int, input ().split ()))


def num ():
	return map (int, input ().split ())


def nu ():
	return int (input ())


def find_gcd ( x, y ):
	while (y):
		x, y = y, x % y
	return x


def solve ():
	t = 1
	for it in range (t):
		n,m,k=num()
		a=li()
		a.sort()
		hh=a[n-1]
		h2=a[n-2]
		op=m//(k+1)
		po=m%(k+1)
		ans=op*k*hh+op*h2+po*hh
		print(ans)



def __starting_point():
	solve ()
__starting_point()
