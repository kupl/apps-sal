from math import inf
import heapq

n, m, k = map(int, input().split(' '))

edge = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split(' '))
    edge[a - 1].append((i, b - 1))
    edge[b - 1].append((i, a - 1))

d = [inf for _ in range(n)]
d[0] = 0

q = [0 for _ in range(n)]
f = 0
r = 1
while f < r:
    i = q[f]
    f += 1
    for (_, j) in edge[i]:
        if d[j] == inf:
            d[j] = d[i] + 1
            q[r] = j
            r += 1


pre = [[] for _ in range(n)]

for i in range(n):
    for (ind, j) in edge[i]:
        if d[j] == d[i] - 1:
            pre[i].append((ind, j))


s = [0 for _ in range(n)]
top = n
sol = []
while top > 0:
    if top == n:
        u = ['0' for _ in range(m)]
        for i in range(1, n):
            u[pre[i][s[i]][0]] = '1'
        sol.append("".join(u))
        if len(sol) == k:
            break
        top -= 1
    else:
        s[top] += 1
        if s[top] == len(pre[top]):
            top -= 1
        else:
            top += 1
            if top < n:
                s[top] = -1

print(len(sol))
for x in sol:
    print(x)
