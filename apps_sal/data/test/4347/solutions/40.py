import sys
input = sys.stdin.readline
I = lambda : list(map(int,input().split()))

def fact(n):
	if n<=1:
		return 1
	return n*fact(n-1)

n,=I()
print(fact(n-1)//(n//2))
