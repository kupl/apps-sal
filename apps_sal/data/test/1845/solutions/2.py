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

l.sort()

s=sum(l)

ms=s
for num in l:
	for j in range(1,num//2+1):
		if num%j==0:
			newnum=num//j
			newsum=s-num+newnum-l[0]+j*l[0]

			ms=min(newsum,ms)


print(ms) 

