import sys
import math
input = sys.stdin.readline

n,m=map(int,input().split())
alist=list(map(int,input().split()))
blist=list(map(int,input().split()))
alist.sort()
blist.sort()

minx=math.inf
for i in range(n):
	diff=(blist[0]-alist[i]+m)%m
	# print("diff",diff)
	arr=[]
	for j in range(n):
		arr.append((alist[j]+diff)%m)
	arr.sort()
	# print(arr)
	flag=True
	for j in range(n):
		if arr[j]!=blist[j]:
			flag=False
			break
	if flag:
		minx=min(minx,diff)

print(minx)
