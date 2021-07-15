import io, sys, atexit, os
import math as ma
from decimal import Decimal as dec
from itertools import permutations
from itertools import combinations


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


def lcm ( x, y ):
	gg = find_gcd (x, y)
	return (x * y // gg)


def printDivisors ( n ):
	# Note that this loop runs till square root
	i = 1
	cc=0
	while i <= ma.sqrt (n):

		if (n % i == 0):

			# If divisors are equal, print only one
			if (n / i == i):
				cc+=1
			else:
				# Otherwise print both
				cc+=2
		i = i + 1
	return cc

mm = 1000000007
yp = 0


def solve ():
	t = 1
	for tt in range (t):
		n=nu()
		a=li()
		gg=0
		for i in range(n):
			gg=find_gcd(gg,a[i])
		cc=0
		print(printDivisors(gg))




def __starting_point():
	solve ()
__starting_point()
