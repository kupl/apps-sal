from collections import defaultdict as dd
import math
import heapq


def nn():
	return int(input())

def li():
	return list(input())

def mi():
	return list(map(int, input().split()))

def lm():
	return list(map(int, input().split()))






n, k=mi()

songs=[]

for i in range(n):
	songs.append(lm())


songs.sort(key=lambda x:-x[1])

h=[]
maxsofar=0
newlen=0
#print(songs)
for i in range(n):
	beauty=songs[i][1]
	heapq.heappush(h,songs[i][0])
	removed=0
	if i>=k:
		removed=heapq.heappop(h)
	
	newlen=newlen+songs[i][0]-removed
	maxsofar=max(maxsofar,newlen*beauty)
	#print(newlen,maxsofar)
print( maxsofar)
	
		

