from collections import deque
n = int(input())
e = [[] for i in range(n)]
for i in range(n - 1):
    (a, b, c) = map(int, input().split())
    a -= 1
    b -= 1
    e[a].append([b, c])
    e[b].append([a, c])
(m, k) = map(int, input().split())
k -= 1
d = [-1] * n
d[k] = 0
q = deque()
q.append([k, 0])
while q:
    (f, cc) = q.pop()
    for (t, nc) in e[f]:
        if d[t] == -1:
            d[t] = cc + nc
            q.append([t, d[t]])
for i in range(m):
    (f, t) = map(int, input().split())
    f -= 1
    t -= 1
    print(d[f] + d[t])
