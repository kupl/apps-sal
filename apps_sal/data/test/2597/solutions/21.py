import sys
input=sys.stdin.readline
y=int(input())
for i in range(y):
	n=int(input())
	l=list(map(int,input().split())) 
	l=sorted(l)
	z=[]
	for i in range(n):
		x1=min(l[i],n-i)
		z.append(x1)
	print(max(z))

