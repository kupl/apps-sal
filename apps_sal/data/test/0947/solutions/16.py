import sys
input = sys.stdin.readline
I = lambda : list(map(int,input().split()))

t,=I()
for _ in range(t):
	n,=I()
	a=b=0
	for i in range(2,int(n**0.5)+1):
		if n%i==0:
			a=n//i;b=n//i*(i-1)
			break
	if a==0:
		a=1;b=n-1
	print(a,b)
