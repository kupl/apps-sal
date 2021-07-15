'''input
3
1
3
7
'''
import math	
def solve():
	n = int(input())
	l = [i for i in range(1,n+1)]
	l = l[::-1]
	for i in l:
		print(i,end=" ")
	print()
t = 1
t = int(input())
while t > 0:
	t-=1
	solve()
