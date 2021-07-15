from collections import defaultdict as dd
import math
import sys
import heapq
import copy
input=sys.stdin.readline
def nn():
	return int(input())

def li():
	return list(input())

def mi():
	return list(map(int, input().split()))

def lm():
	return list(map(int, input().split()))


def solve():
	n = nn()

	ice= lm()

	ice.sort()
	out = []
	for i in range(n):
		if i%2==1:
			out.append(ice[i//2])

		else:
			out.append(ice[((i//2+n//2))])
	good= 0
	for i in range(n-1):
		if i%2==1:
			if out[i]<out[i+1] and out[i]<out[i-1]:
				good+=1
	print(good)
	print(*out)
solve()

