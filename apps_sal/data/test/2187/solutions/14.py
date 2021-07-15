from collections import defaultdict as dd
import math
import sys
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
	n=nn()
	nums = lm()
	needed = 0
	for i in reversed(list(range(1,n))):
		if nums[i]<nums[i-1]:
			needed+= nums[i-1]-nums[i]

	print(needed)

q=nn()
for _ in range(q):
	solve()

