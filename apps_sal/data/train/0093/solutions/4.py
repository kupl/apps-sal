from math import *
import os, sys
from bisect import *
from io import BytesIO

#input = BytesIO(os.read(0, os.fstat(0).st_size)).readline
sys.setrecursionlimit(10 ** 9)
#sys.stdin = open("moobuzz.in", 'r')
#sys.stdout = open("moobuzz.out", 'w')

for i in range(int(input())):
	n, m = list(map(int, input().split()))
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	d = {}
	for i in range(n):
		d[a[i]] = i
	
	ans = 0
	mx = 0
	for i in range(m):
		if mx < d[b[i]]:
			ans += 2 * (d[b[i]] - i) + 1
			mx = d[b[i]]
		else:
			ans += 1
	print(ans)

