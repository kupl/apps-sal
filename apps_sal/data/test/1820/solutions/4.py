import sys
import math
def II():
	return int(sys.stdin.readline())

def LI():
	return list(map(int, sys.stdin.readline().split()))

def MI():
	return map(int, sys.stdin.readline().split())

def SI():
	return sys.stdin.readline().strip()
t = II()
for q in range(t):
	n = II()
	a = sorted(LI())
	if a[0]+a[1]<=a[-1]:
		print(1,2,n)
	else:
		print(-1)
