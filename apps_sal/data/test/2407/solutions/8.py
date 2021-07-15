import sys
import math
input = sys.stdin.readline

arr=[]
n=0
r=0

def check(k):
	if arr[n-k-1]-k*r>0:
		return False
	return True
	
def binarySearch (l, r): 
  
	if r >= l: 
  
		mid = l + (r - l)//2

		if check(mid):
			if r==l:
				return l
				
			return(binarySearch(l, mid))

		else:
			return binarySearch(mid + 1, r) 
  
	else: 
		return n
  

q=int(input())
for i in range(q):
	n,r=map(int,input().split())
	l=list(map(int,input().split()))
	arr=list(set(l))
	n=len(arr)
	arr.sort()

	print(binarySearch(1,n-1))
