import sys
import math
input = sys.stdin.readline

q=int(input())
for i in range(q):
	n,m=list(map(int,input().split()))
	r=[0]*n
	c=[0]*m
	arr=[]
	for i in range(n):
		arr.append(input())

	for i in range(n):
		for j in range(m):
			if arr[i][j]==".":
				r[i]+=1
				c[j]+=1
	minn=1000000000
	for i in range(n):
		for j in range(m):
			if arr[i][j]==".":
				minn=min(minn,r[i]+c[j]-1)
			else:
				minn=min(minn,r[i]+c[j])

	print(minn)
		

