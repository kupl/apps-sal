from collections import deque
import sys
sys.setrecursionlimit(10**5)
n, m, s = map(int, input().split())
s -= 1
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)

seen = [False] * n
li = deque()


def visit(node):
    if not seen[node]:
        seen[node] = True
        for c_node in graph[node]:
            visit(c_node)
        li.appendleft(node)


for i in range(n):
    visit(i)
seen = [False] * n
cnt = 0
li2 = list(li)
visit(s)
for i in li2:
    if seen[i]:
        continue
    visit(i)
    cnt += 1
print(cnt)
