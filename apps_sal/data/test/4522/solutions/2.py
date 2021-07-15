'''input
3 3
1 2 1
2 3 2
1 3 2
'''
from sys import stdin
from copy import deepcopy
from collections import deque, defaultdict


def find_parent(n):
	nonlocal parent
	node = n
	while parent[node] != node:
		node = parent[node]
	parent[n] = node
	return parent[n]


def combination(num):
	return (num * (num - 1)) // 2

# main starts
n, m = list(map(int, stdin.readline().split()))
graph = defaultdict(list)
edges = []
for _ in range(n - 1):
	edges.append(list(map(int, stdin.readline().split())))

queries = list(map(int, stdin.readline().split()))

edges.sort(key = lambda x:x[2], reverse = True)
parent = dict()
count = dict()
for i in range(1, n + 1):
	parent[i] = i
	count[i] = 1

ans = [0] * (200001)
while len(edges) > 0:
	u, v, w = edges.pop()

	if u > v:
		u, v = v, u

	pv = find_parent(v)
	pu = find_parent(u)
	ans[w] -= (combination(count[pu]) + combination(count[pv]))
	ans[w] += combination(count[pu] + count[pv])
	count[pu] += count[pv]
	count[pv] = 0
	parent[pv] = parent[pu]
		
	# print(u, v, w)
	# print('parent', parent)
	# print('count', count)
	# print(ans)


for i in range(1, len(ans)):
	ans[i] = ans[i - 1] + ans[i]
# print(ans[:10])

for i in queries:
	print(ans[i], end = ' ')




