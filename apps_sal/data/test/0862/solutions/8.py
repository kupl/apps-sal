import math
n=int(input())
l=list(map(int,input().strip().split()))
l1=[]
for x,y in enumerate(l):
	if (y<x):
		m=0
	else:
		m=y-x
	l1.append(math.ceil(m/n))
min1=100000000000000
min2=1000000000000
for i in range(n):
	if l1[i]<min1:
		min1=l1[i]
		min2=i+1
print (min2)
