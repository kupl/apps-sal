'''input
6
011100
5 3
5 5
2 4
3 5
4 2
1 5


'''
import sys
from collections import defaultdict as dd

mod=10**9+7

def ri(flag=0):
	if flag==0:
		return [int(i) for i in sys.stdin.readline().split()]
	else:
		return int(sys.stdin.readline())

n = ri(1)
a = input()

b= []

time = [0 for i in range(5030)]


for i in range(n):
	x,y = ri()
	cur = int(a[i])
	for j in range(y):
		time[j] += cur
	for j in range(5010):
		if j%x==0:
			cur = cur^1
		time[y+j] += cur
		

print(max(time))



