import sys
import math
input = sys.stdin.readline

n=int(input())

arr=list(map(int,input().split()))
maxp=-1
cur=-1
for i in range(n):
	if arr[i]>=0:
		arr[i]=-arr[i]-1
		if arr[i]>maxp:
			maxp=arr[i]
			cur=i

if n%2==0:
	print(*arr)
else:
	if maxp==-1:
		mx=-1
		cr=-1
		for i in range(n):
			if arr[i]<0:
				if abs(arr[i])>mx:
					mx=abs(arr[i])
					cr=i

		arr[cr]=-arr[cr]-1
	else:
		arr[cur]=-arr[cur]-1
	#print(mx,cr)
	print(*arr)
