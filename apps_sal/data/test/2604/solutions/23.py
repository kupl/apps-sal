from sys import stdin
import math

def distance(x,y):
	return abs(math.sqrt(x*x+y*y)) 

def check(x,y,rad):
	dist = distance(x,y)
	if((dist+rad)<=r and dist-rad>=(r-d)):
		return True
	else:
		return False


r,d=list(map(int,input().split()))
n=int(input())
count=0
for u in range(n):
	x,y,rad=list(map(int,input().split()))
	if(check(x,y,rad)):
		count+=1
print(count)
