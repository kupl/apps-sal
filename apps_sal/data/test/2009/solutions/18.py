n = int(input())
r1, c1 = list(map(int, input().split()))
r2, c2 = list(map(int, input().split()))
r1, c1, r2, c2 = r1-1, c1-1, r2-1, c2-1
g = []
for i in range(n):
    g.append(list(map(int, list(input()))))
from_r1 = set()
from_r2 = set()
x = [0, 1, 0, -1]
y = [1, 0, -1, 0]
visited = [[False for i in range(n)] for j in range(n)]

stack = [(r1, c1)]
while stack:
    v = stack.pop()
    if v[0] == r2 and v[1] == c2:
        print(0)
        return
    visited[v[0]][v[1]] = True
    for i in range(4):
        if v[0] + x[i] < n and v[1] + y[i] < n and v[0] + x[i] >= 0 and v[1] + y[i]>= 0 and not visited[v[0] + x[i]][v[1] + y[i]]:
            if g[v[0] + x[i]][v[1] + y[i]] == 0:
                stack.append((v[0]+x[i], v[1]+y[i]))
            else:
                from_r1.add((v[0], v[1]))


visited = [[False for i in range(n)] for j in range(n)]
stack = [(r2, c2)]
while stack:
    v = stack.pop()
    visited[v[0]][v[1]] = True
    for i in range(4):
        if v[0] + x[i] < n and v[1] + y[i] < n and v[0] + x[i] >= 0 and v[1] + y[i] >= 0 and not visited[v[0] + x[i]][v[1] + y[i]]:
            if g[v[0] + x[i]][v[1] + y[i]] == 0:
                stack.append((v[0]+x[i], v[1]+y[i]))
            else:
                from_r2.add((v[0], v[1]))

min_value = 100000000
for i in from_r1:
    for j in from_r2:
        min_value = min((i[0] - j[0])**2 + (i[1] - j[1])**2, min_value)
print(min_value)


