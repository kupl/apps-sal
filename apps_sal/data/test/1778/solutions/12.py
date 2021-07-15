'''input
2
2 1
5 6
'''
import sys
from collections import defaultdict as dd
from itertools import  permutations as pp
from itertools import combinations as cc
from collections import Counter as ccd
from random import randint as rd
from bisect import bisect_left as bl
mod=10**9+7
import heapq

n=int(input())
a=[-int(i) for i in input().split()]+[0]*(100000)
b=[-int(i) for i in input().split()]+[0]*(100000)

heapq.heapify(a)
heapq.heapify(b)

ans1=0
ans2=0

for i in range(2*n):
	if i%2==0:
		#a-turn
		temp1=-heapq.heappop(a)
		temp2=-heapq.heappop(b)
		if temp2>temp1:
			heapq.heappush(a,-temp1)
		else:
			ans1+=temp1
			heapq.heappush(b,-temp2)
	else:
		#b-turn
		temp1=-heapq.heappop(a)
		temp2=-heapq.heappop(b)
		if temp2<temp1:
			heapq.heappush(b,-temp2)
		else:
			ans2+=temp2
			heapq.heappush(a,-temp1)
	#print(ans1,ans2)
print(ans1-ans2)


