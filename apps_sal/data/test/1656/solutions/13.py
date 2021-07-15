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


mm = 1000000007
yp = 0
def solve ():
	t = 1
	for tt in range (t):
		s=input()
		n=len(s)
		l=[0]*n
		for i in range(n-1):
			if(s[i]==s[i+1] and s[i]=="v"):
				l[i]=1
		pre=[0]*n
		suf=[0]*n
		pre[0]=l[0]
		for i in range(1,n):
			pre[i]=pre[i-1]+l[i]
		suf[n-1]=l[n-1]
		for i in range(n-2,-1,-1):
			suf[i]=suf[i+1]+l[i]
		ans=0
		for i in range(n):
			if(s[i]=="o"):
				if(i-1>=0 and i+1<n):
					ans+=pre[i-1]*suf[i+1]
		print(ans)

def __starting_point():
	solve ()
__starting_point()
