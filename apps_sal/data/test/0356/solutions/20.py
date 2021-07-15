'''input
3
1 2 3
3
1 2 3
'''
import sys
from collections import defaultdict as dd
from itertools import  permutations as pp
from itertools import combinations as cc
from collections import Counter as ccd
from random import randint as rd
from bisect import bisect_left as bl
mod=10**9+7


n=int(input())
a=[int(i) for i in input().split()]
m=int(input())
b=[int(i) for i in input().split()]

for i in range(1,n):
	a[i]+=a[i-1]
for i in range(1,m):
	b[i]+=b[i-1]

if a[-1]!=b[-1]:
	print(-1)
else:
	a=set(a)
	b=set(b)

	ans=len(a.intersection(b))

	if ans==0 :
		print(-1)
	else:
		print(ans)


