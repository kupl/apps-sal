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


mm = 1000000007
yp = 0
def solve ():
	t = 1
	for tt in range (t):
		n=nu()
		cc=0
		s=str(bin(n))[2:]
		xp=[]
		pp=0
		while(cc<=40):
			fl=False
			ind=-1
			for i in range(len(s)):
				if(s[i]=="0"):
					fl=True
					ind=i
					break
			if(fl==False):
				break
			cc+=1
			if(pp==1):
				pp^=1
				n+=1
				s = str (bin (n)) [ 2: ]
			else:
				pp ^= 1
				gg=pow(2,len(s)-ind)-1
				xp.append(len (s) - ind)
				n^=gg
				s = str (bin (n)) [ 2: ]
		print(cc)
		print(*xp)


def __starting_point():
	solve ()
__starting_point()
