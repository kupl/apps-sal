'''input
2
3 2
1 3 5
4 1
5 2 3 5

'''
import sys
from collections import defaultdict as dd
from itertools import  permutations as pp
from itertools import combinations as cc
from collections import Counter as ccd
from random import randint as rd
from bisect import bisect_left as bl
from  heapq import heappush as hpush
from heapq import heappop as hpop
mod=10**9+7

def ri(flag=0):
	if flag==0:
		return [int(i) for i in sys.stdin.readline().split()]
	else:
		return int(sys.stdin.readline())


for _ in range(ri(1)):
	n , r =ri()
	a = ri()
	a = list(set(a))
	a.sort()
	ans =0
	cur = 0
	start = a[-1]
	for i in range(len(a)-1,-1,-1):
		if a[i]-cur>0:
			cur+=r
			ans+=1
	print(ans)





