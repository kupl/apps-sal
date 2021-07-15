# stdin=open('input.txt')
from sys import stdin, stdout
def input():
	return stdin.readline()[:-1]


# stdout=open('output.txt',mode='w+')

# def print(x, end='\n'):
# 	stdout.write(str(x) +end)


# a, b = map(int, input().split())

# l = list(map(int, input().split()))

# n = int(input())





# CODE BEGINS HERE.................

# import copy
import math
# import sys
# sys.setrecursionlimit(10**7)

m, n = list(map(int, input().split()))

days = []
for i in range(m):
	days.append(set(list(map(int, input().split()))[1:]))
possible = True
for i in range(m):
	for j in range(i):
		if not days[i].intersection(days[j]):
			possible = False
			break
	if not possible:
		break

if possible:
	print('possible')
else:
	print('impossible')

#CODE ENDS HERE....................


#stdout.close()


