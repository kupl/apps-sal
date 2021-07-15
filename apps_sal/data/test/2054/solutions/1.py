from collections import defaultdict as dd
import math
import sys
import string
input=sys.stdin.readline
def nn():
	return int(input())

def li():
	return list(input())

def mi():
	return list(map(int, input().split()))

def lm():
	return list(map(int, input().split()))

q=nn()
for _ in range(q):

	d, s = mi()

	m = min(d,s)

	print(min(m,(d+s)//3))

