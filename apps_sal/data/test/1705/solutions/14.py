'''input
4
1 0 0 1
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

n=ri(1)
a=ri()
one=0
two=0

for i in a:
	if i==0:
		one+=1
	else:
		two+=1

idx=-1
for i in range(n):
	if a[i]==0:
		one-=1
		if one==0:
			idx=i+1
			break
	else:
		two-=1
		if two==0:
			idx=i+1
			break
print(idx)
