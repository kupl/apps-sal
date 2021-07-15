import sys
import math
input = sys.stdin.readline

arr=[]
for i in range(1,100000):
	arr.append(i*(i+1)//2)

def bs(l, r, x):
	if r>=l:
		mid = l + (r-l)//2
		if arr[mid]<=x and arr[mid+1]>x:
			return mid

		elif arr[mid]>x:
			return bs(l, mid-1, x)

		else:
			return bs(mid+1, r, x)

t=int(input())
for i in range(t):
	n=int(input())

	d=bs(0,len(arr)-1,n)
	diff=n-arr[d]
	#print(d,diff)

	ans=["1","3","3"]
	for j in range(diff):
		ans.append("7")
	for j in range(d):
		ans.append("3")
	ans.append("7")

	print(''.join(ans))

