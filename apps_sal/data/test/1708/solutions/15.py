'''input
6 6
6 6 6 6 6 6
6 66 666 6666 66666 666666
1 6
2 13
3 6
4 11
5 6
6 6
'''
import sys
from collections import defaultdict as dd
from itertools import  permutations as pp
from itertools import combinations as cc
from collections import Counter as ccd
from random import randint as rd
from bisect import bisect_left as bl
import heapq
mod=10**9+7

def ri(flag=0):
	if flag==0:
		return [int(i) for i in sys.stdin.readline().split()]
	else:
		return int(sys.stdin.readline())

n,m=ri()
a=ri()
c=ri()

hee=[]

for i in range(n):
	heapq.heappush(hee,(c[i],i))

avail=a[:]

for i in range(m):
	cost=0
	t,d=ri()
	t-=1
	fm=0
	if avail[t]>=d:
		avail[t]=avail[t]-d
		cost+=(d*c[t])
	else:
		rem=d-avail[t]
		cost=avail[t]*c[t]
		avail[t]=0
		while rem>0:
			try:
				nowc,nowi=heapq.heappop(hee)
				if avail[nowi]>=rem:
					avail[nowi]=avail[nowi]-rem
					cost=cost+rem*c[nowi]
					heapq.heappush(hee,(c[nowi],nowi))
					rem=0
				else:
					cost=cost+avail[nowi]*c[nowi]
					mk=rem-avail[nowi]
					avail[nowi]=0
					rem=mk
			except:
				fm=1
				break
	if fm==0:
		print(cost)
	else:
		print(0)





