import math
import sys
input = sys.stdin.readline
for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	group = [0]*31
	for i in a:
		x = int(math.log2(i))
		group[x] += 1
	ans = 0
	for i in group:
		ans += ((i)*(i-1))//2
	print (ans)

