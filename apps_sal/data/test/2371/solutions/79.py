import sys
sys.setrecursionlimit(10**8)

def sort(a):
	a.sort()

def rev(a):
	a.reverse()

def sd():
	return int(input())

def _sd():
	return list(map(int,input().split()))

def sa():
	return list(map(int,input().split()))

def ss():
	return input()

def sf():
	return float(input())
 
def main():
	N,Z,W=_sd()
	a=sa()
	if(N>1):
		print((max(abs(a[N-1]-W),abs(a[N-2]-a[N-1]))))
	else:
		print((abs(a[0]-W)))
main()

