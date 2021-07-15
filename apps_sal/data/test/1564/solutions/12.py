'''input
8
babbaabb
abababaa



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

a= input()
b = input()
one =[] #ab
two=[]  #ba

for i in range(n):
	if a[i]==b[i]:
		pass
	else:
		if a[i]=="a":
			one.append(i+1)
		else:
			two.append(i+1)

if (len(one)+len(two)) %2 ==1:
	print(-1)
else:
	k = len(one)+len(two)
	steps=[]

	for i in range(0,len(one),2):

		if i+1<len(one):
			steps.append((one[i],one[i+1]))

	for i in range(0,len(two),2):
		if i+1<len(two):
			steps.append((two[i],two[i+1]))

	#print(one,two)
	if len(one)%2==1:

		steps.append((one[-1],one[-1]))
		steps.append((one[-1],two[-1]))

	print(len(steps))
	for i in steps:
		print(*i)






