from collections import deque
s = 0
n = int(input())
ls = [[] for i in range(n + 1)]
for i in range(1, n):
    a, b = list(map(int, input().split()))
    ls[a].append(b)
    ls[b].append(a)
arr = [0 for i in range(n + 1)]
q = deque()
q.append([1, 1, 0])
while q:
    x = q.pop()
    node = x[0]
    arr[node] = 1
    to_explore = []
    for i in ls[node]:
        if arr[i] == 0:
            to_explore.append(i)

    if len(to_explore) == 0:
        s = s + x[1] * x[2]
        continue
    n = len(to_explore)
    for i in to_explore:
        q.append([i, x[1] / n, x[2] + 1])
print(s)
