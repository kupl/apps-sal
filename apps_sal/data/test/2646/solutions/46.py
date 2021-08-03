from collections import deque

n, m = map(int, input().split())
V = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    V[a].append(b)
    V[b].append(a)

reach = [-1] * (n + 1)
reach[1] = 0
q = deque([])
q.append(1)

while q:
    x = q.popleft()

    for y in V[x]:
        if reach[y] == -1:
            reach[y] = x
            q.append(y)

print("Yes")
for i in range(2, n + 1):
    print(reach[i])
