'''input
3 1
0 1 2
'''
from sys import stdin
import collections
import math
import queue


# main starts
n, k = list(map(int, stdin.readline().split()))
distance = list(map(int, stdin.readline().split()))

# n = 65535; k = 3
# distance = []
# for i in range(16):
# 	for j in range(2 **i):
# 		distance.append(i)

for i in range(n):
	distance[i] = [i + 1, distance[i]]

distance = sorted(distance, key = lambda x:x[1])

if distance[0][1] != 0:
	print(-1)
	return

edges = []
i = 1
buff = collections.deque()
buff.append(distance[0])

while len(buff) > 0 and i < n:
	prev_node, prev_dist = buff.popleft()

	count = 0
	while i < n:
		if prev_dist + 1 == distance[i][1]:
			if (count == k and prev_dist == 0) or (count == k - 1 and prev_dist != 0):
				break
			edges.append([prev_node, distance[i][0]])
			buff.append(distance[i])
			count += 1
			i += 1


		elif prev_dist + 2 == distance[i][1]:
			break
		else:	
			print(-1)
			return
if i != n:
	print(-1)
	return
print(len(edges))
for i in edges:
	print(*i)
