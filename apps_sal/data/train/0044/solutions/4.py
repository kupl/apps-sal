import sys,math
# import re
# from heapq import *
# from collections import defaultdict as dd
# from collections import Counter as cc
# sys.setrecursionlimit(10**6)#thsis is must
mod = 10**9+7; md = 998244353
input = lambda: sys.stdin.readline().strip()
inp = lambda: list(map(int,input().split()))
#______________________________________________________
for _ in range(int(input())):
	n = int(input())
	t = 4*n
	for i in range(n):
		print(t,end = " ")
		t-=2
	print()
