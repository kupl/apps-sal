'''input
5
0 1 2 3 
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

a.sort()

k=dd(int)

for i in a:
	k[i]+=1

f=1
for i in k:
	if k[i]>2:
		f=0

one=[]
two=[]

for i in k:
	if k[i]==1:
		one.append(i)

	elif k[i]==2:
		one.append(i)
		two.append(i)

if f:
	print("YES")
	print(len(one))
	one.sort()
	print(*one)
	print(len(two))
	two.sort(reverse=True)
	print(*two)
else:
	print("NO")
