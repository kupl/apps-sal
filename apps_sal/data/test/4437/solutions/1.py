'''input
2
aa


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



n = ri(1)
a = list(input())
ans =0

for i in range(0,n,2):
	if a[i]!=a[i+1]:
		pass
	else:
		if a[i]=="a":
			a[i]="b"
		else:
			a[i]="a"
		ans+=1

print(ans)
print("".join(a))

