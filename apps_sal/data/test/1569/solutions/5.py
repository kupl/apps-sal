from sys import *
from collections import *
s = stdin.read().split()
d = list(map(int, s))
(n, m) = d[:2]
g = [[] for i in range(n + 1)]
for j in range(m):
    i = 3 * j + 2
    g[d[i]].append((d[i + 1], d[i + 2], j))
    g[d[i + 1]].append((d[i], d[i + 2], j))
(u, v) = ([-1] * n + [0], [1000000000.0] * n + [0])
(x, y) = ([0] * (n + 1), [0] * (n + 1))
q = deque([n])
while q:
    a = q.popleft()
    for (b, k, i) in g[a]:
        if v[b] == 1000000000.0:
            q.append(b)
        if v[b] > v[a] and u[b] < u[a] + k:
            v[b] = v[a] + 1
            u[b] = u[a] + k
            (x[b], y[b]) = (a, i)
(a, t) = (1, [0] * m)
while a != n:
    (t[y[a]], a) = (1, x[a])
l = []
for j in range(m):
    i = 3 * j + 2
    if d[i + 2] != t[j]:
        l.append(' '.join([s[i], s[i + 1], str(t[j])]))
print(len(l))
print('\n'.join(l))
