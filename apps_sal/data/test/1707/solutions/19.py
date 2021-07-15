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
def abs_int(a):
	return abs(int(a))

n = int(input())
a = list(map(abs_int, input().split()))

a.sort()
# print(a)

ptr = 0
half = -1
gt_than_half = [0] * n
for i in range(n):
	half = math.ceil(a[i]/2)
	while a[ptr] < half:
		ptr += 1
	gt_than_half[i] = i - ptr
# print(gt_than_half)

a.reverse()
# print(a)

ptr = 0
twice = -1
lt_than_twice = [0] * n
for i in range(n):
	twice = 2 * a[i]
	while a[ptr] > twice:
		ptr += 1
	lt_than_twice[i] = i - ptr
# print(lt_than_twice)

print((sum(gt_than_half) + sum(lt_than_twice))//2)


#CODE ENDS HERE....................


#stdout.close()


