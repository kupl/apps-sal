import math as ma
import sys
from decimal import Decimal as dec
from itertools import permutations


def li():
	return list(map(int , input().split()))


def num():
	return map(int , input().split())


def nu():
	return int(input())


n,s=num()
cc=0
for i in range(n,0,-1):
	cc+=s//i
	s=s%i
print(cc)
