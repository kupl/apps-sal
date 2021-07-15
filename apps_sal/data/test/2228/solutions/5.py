
import math
from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(100000)
def put():  return  map(int, stdin.readline().split())
for _ in range(1):
	n=int(input())
	start=[]
	end=[]
	for i in range(n):
		a,b=put()
		start.append(a)
		end.append(b)
	start.sort()
	end.sort()
	numalive=0
	startyear=0
	indstart=0
	indend=0
	mx=0
	while(indstart<n ):
		if(start[indstart]<end[indend]):
			numalive+=1
			indstart+=1
			if(numalive>mx):
				mx=max(mx,numalive)
				startyear=start[indstart-1]
		elif(start[indstart]==end[indend]):
			indstart+=1
			indend+=1
		else:
			numalive-=1
			indend+=1
	print(startyear,mx)
