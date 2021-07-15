#!/usr/bin/env python3

from collections import deque

# pre(u) -- to do first at u
# proc(u, v) -- to do before switching from u (parent) to v (child)
# post(u) -- to do before switching to parent of u
def nrDFS(u, tos, pre, proc, post):
	n = len(tos)
	visited = [False for _ in range(n)]
	def go_to(cur, nxt):
		proc(cur, nxt)
		visited[nxt] = True
		pre(nxt)
		return nxt, 0
	stack = deque()
	cur, i = go_to(u, u)
	while True:
		if i < len(tos[cur]):
			if not visited[tos[cur][i]]:  # go to tos[cur][i]
				stack.append((cur, i))
				cur, i = go_to(cur, tos[cur][i])
			else:
				i += 1
				continue
		else:  # return to parent
			post(cur)
			if len(stack) == 0:
				break
			cur, i = stack.pop()
			i += 1
			continue



n = int(input().strip())
tos = [[] for _ in range(n)]
for _ in range(n - 1):
	[u, v] = list(map(int, input().strip().split()))
	tos[u - 1].append(v - 1)
	tos[v - 1].append(u - 1)

if n % 2 == 1:
	print(-1)
	return

def pre(u):
	pass

parent = [0 for _ in range(n)]
def proc(u, v):
	parent[v] = u

s = [0 for _ in range(n)]
def post(u):
	s[u] = 1 + sum(s[v] for v in tos[u] if v != parent[u])
		

nrDFS(0, tos, pre, proc, post)
print(n - 1 - sum(si % 2 for si in s))


