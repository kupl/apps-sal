from collections import defaultdict as dd
import math
def nn():
	return int(input())

def li():
	return list(input())

def mi():
	return list(map(int, input().split()))

def lm():
	return list(map(int, input().split()))



n=nn()

l=lm()

maxsofar=0
days=1

for i, num in enumerate(l):
	maxsofar=max(maxsofar, num)
	#print(maxsofar)
	if maxsofar==i+1 and i<len(l)-1:
		days+=1 

print(days)

