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


def lcm ( x, y ):
	gg = find_gcd (x, y)
	return (x * y // gg)


mm = 1000000007
yp = 0

def solve ():
	t = 1
	for _ in range (t):
		h,w=num()
		xp=[0]*h
		for i in range(h):
			xp[i]=[0]*w
			lp=input()
			for j in range(len(lp)):
				if(lp[j]=="."):
					xp[i][j]=0
				else:
					xp[i][j]=1
		fl=False
		for i in range(h):
			for j in range(w):
				if(xp[i][j]==1):
					if((i-1>=0 and xp[i-1][j]==1) and (i+1<h and xp[i+1][j]==1) and (j-1>=0 and xp[i][j-1]==1) and (j+1<w and xp[i][j+1]==1)):
						fl=True
						xp[i][j]=2
						for k in range(i-1,-1,-1):
							if(xp[k][j]==1):
								xp[k][j]=2
							else:
								break
						for k in range(i+1,h):
							if (xp [ k ] [ j ] == 1):
								xp [ k ] [ j ] = 2
							else:
								break
						for k in range(j-1,-1,-1):
							if (xp [ i ] [ k ] == 1):
								xp [ i ] [ k ] = 2
							else:
								break
						for k in range(j+1,w):
							if (xp [ i ] [ k ] == 1):
								xp [ i ] [ k ] = 2
							else:
								break
						break
			if(fl):
				break
		if(fl):
			op=True
			for i in range(h):
				for j in range(w):
					if(xp[i][j]==1):
						op=False
			if(op==False):
				print("NO")
			else:
				print("YES")
		else:
			print("NO")

def __starting_point():
	solve ()
__starting_point()
