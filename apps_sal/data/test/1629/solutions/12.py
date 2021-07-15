'''input
3 3
2 3 1
'''
from sys import stdin, setrecursionlimit
import math
from collections import defaultdict, deque

setrecursionlimit(15000)


def transform(arr, ans):
	for i in range(len(arr)):
		arr[i] -= ans 


def find_index(x, arr, ):
	i = x - 1 

	while True:
		if arr[i] == 0:
			break
		arr[i] -= 1
		i -= 1
		if i == -1:
			i = n - 1
	return i


def add_remain(x, arr, index):
	i = x - 1
	count = 0
	while True:
		if i == index:
			break
		count += 1
		i -= 1
		if i == -1:
			i = len(arr) - 1
	return count


# main starts
n, x = list(map(int, stdin.readline().split()))
arr = list(map(int, stdin.readline().split()))
carr = arr[:]
mn = min(arr)
transform(carr, mn)
ans  = mn * n
index = find_index(x, carr)
ans += add_remain(x, arr, index)

for i in range(n):
	arr[i] -= mn
arr[index] = ans
i = x - 1
while True:
	if i == index:
		break
	arr[i] -= 1
	i -= 1
	if i < 0:
		i = n - 1
print(*arr)


