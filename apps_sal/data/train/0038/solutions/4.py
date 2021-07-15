from math import *
import os, sys
from bisect import *
from io import BytesIO

#input = BytesIO(os.read(0, os.fstat(0).st_size)).readline
sys.setrecursionlimit(10 ** 9)
#sys.stdin = open("moobuzz.in", 'r')
#sys.stdout = open("moobuzz.out", 'w')

for _ in range(int(input())):
	n, k1, k2 = list(map(int, input().split()))
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	if max(a) > max(b):
		print("YES")
	else:
		print("NO")

