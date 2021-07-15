
from collections import deque, defaultdict
import copy
import bisect
#sys.setrecursionlimit(10 ** 9)
import math
import heapq

import sys
def input():
	return sys.stdin.readline().strip()

N = int(input())
P = list(map(int, input().split()))
X = list(map(int, input().split()))

tree = [[] for i in range(N)]


for i in range(N - 1):
	tree[P[i] - 1].append(i + 1)

sum_list = [0]*N
que = deque([0])
que2 = deque([0])
while len(que) > 0:
	node = que.popleft()
	if len(tree[node]) > 0:
		for edge in tree[node]:
			que.append(edge)
			que2.append(edge)

for i in range(N - 1, -1, -1):
	node = que2[i]
	if len(tree[node]) > 0:
		for edge in tree[node]:
			sum_list[node] += sum_list[edge]
	sum_list[node] += X[node]

score = [[0,0] for i in range(N)]
for i in range(N - 1, -1, -1):
	node = que2[i]
	if len(tree[node]) == 0:
		score[node] = [X[node], 0]
	else:
		rest = X[node]
		dp = [[0 for i in range(len(tree[node]) + 1)] for j in range(rest + 1)]
		dp[0][0] = 1
		for x in range(rest + 1):
			for n in range(1, len(tree[node]) + 1):
				dp[x][n] = 0
				if x - score[tree[node][n-1]][0] >= 0:
					dp[x][n] = dp[x - score[tree[node][n-1]][0]][n - 1]
				if x - score[tree[node][n-1]][1] >= 0:
					dp[x][n] = dp[x][n] | dp[x - score[tree[node][n-1]][1]][n - 1]
		judge = 0
		#print(dp)
		for x in range(rest, -1, -1):
			#print(x, len(tree[node]))
			if dp[x][len(tree[node])] == 1:
				judge = 1
				under_sum = 0
				for n in range(len(tree[node])):
					under_sum += sum(score[tree[node][n]])
				under_sum += rest - x
				under_sum -= X[node]
				score[node] = [X[node], under_sum]
				break
		if judge == 0:
			print("IMPOSSIBLE")
			return
print("POSSIBLE")
