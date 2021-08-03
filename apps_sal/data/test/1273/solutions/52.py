import sys
from collections import deque

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
g = [[] for _ in range(n)]
e = []
for _ in range(n - 1):
    a, b = list(map(int, input().split()))
    g[a - 1].append(b - 1)
    e.append(b - 1)

stack = deque([0])
stack.append(0)
ans = [0 for _ in range(n)]
while stack:
    v = stack.popleft()
    c = 1
    for nv in g[v]:
        if ans[v] == c:
            c += 1
        ans[nv] = c
        c += 1
        stack.append(nv)

print((max(ans)))
for i in e:
    print((ans[i]))
