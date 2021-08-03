from collections import deque
n = int(input())
a = [list(map(int, input().split())) + [0] for i in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j] -= 1
l = [0] * n
d = [0] * n
Q = deque(range(n))
while Q:
    p = Q.popleft()
    q = a[p][l[p]]
    if a[q][l[q]] == p:
        m = max(d[p], d[q]) + 1
        d[p] = m
        d[q] = m
        l[p] += 1
        l[q] += 1
        Q.append(p)
        Q.append(q)
for i in l:
    if i != n - 1:
        print(-1)
        return()
print(max(d))
