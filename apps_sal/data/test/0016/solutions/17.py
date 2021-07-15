from collections import defaultdict as dd
import math
def nn():
	return int(input())

def li():
	return list(input())

def mi():
	return list(map(int, input().split()))

def lm():
	return list(map(int, input().split()))


c1=nn()
c2=nn()
c3=nn()
c4=nn()

if not c1==c4:
	print(0)
elif c1==0 and not c3==0:
	print(0)
else:
	print(1)

