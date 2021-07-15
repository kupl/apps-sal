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


def solve():
	n = nn()

	print((n+2)//2)

q=nn()

for _ in range(q):
	solve()

