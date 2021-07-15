import sys
import math
input = sys.stdin.readline

n,x,y=map(int,input().split())

a=list(map(int,input().split()))

for i in range(n):
	flag=True
	for j in range(1,x+1):
		if i-j>=0 and a[i]>a[i-j]:
			flag=False
			break
	for j in range(1,y+1):
		if i+j<n and a[i]>a[i+j]:
			flag=False
			break

	if flag:
		print(i+1)
		break
