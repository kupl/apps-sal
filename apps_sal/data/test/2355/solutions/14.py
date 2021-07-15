'''input
1
6 0
'''
# practicing a skill right after sleep improves it a lot quickly
from sys import stdin, setrecursionlimit


# main starts
t = int(stdin.readline().strip())
for _ in range(t):
	n, p = list(map(int, stdin.readline().split()))
	count = 0
	flag = 0
	for i in range(1, n + 1):
		if flag == 1:
			break
		for j in range(i + 1, n + 1):
			if count == 2 * n + p:
				flag = 1
				break
			print(i, j)
			count += 1

