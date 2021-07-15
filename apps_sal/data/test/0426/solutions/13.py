'''input
1 0
1

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


n , k = ri()
a = input()
b = list(a)
cnt = 0
for i in range(n):
	if cnt>=k:
		break
	if i==0:
		if b[i]!="1":
			b[i]="1"
			cnt+=1
	else:
		if b[i]!="0":
			b[i]="0"
			cnt+=1
if n==1 and k>=1:
	print("0")
else:
	print("".join(b))

