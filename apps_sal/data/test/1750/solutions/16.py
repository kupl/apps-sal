from math import ceil, sqrt, factorial, gcd
from collections import deque
from sys import stdin
def input(): return stdin.readline().strip()


n = int(input())
graph = {i: set() for i in range(n)}
for i in range(n - 1):
    a, b = list(map(int, input().split()))
    graph[a - 1].add(b - 1)
    graph[b - 1].add(a - 1)
ma = 0
for i in graph:
    if len(graph[i]) + 1 > ma:
        ma = len(graph[i]) + 1
        x = i
print(ma)
ans = [0 for i in range(n)]
stack = [x]
papa = [0 for i in range(n)]
while stack:
    x = stack.pop()
    # z=set(s)
    a = 1
    if ans[x] == 0:
        ans[x] = 1
        z = [1]
    else:
        z = []
        z.append(ans[x])
        z.append(ans[papa[x]])
    for j in graph[x]:
        while 1:
            if a in z:
                a += 1
            else:
                ans[j] = a
                a += 1
                break
        stack.append(j)
        graph[j].remove(x)
        papa[j] = x
print(*ans)
