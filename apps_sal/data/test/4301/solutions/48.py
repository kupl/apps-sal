from copy import copy
(n, *a) = list(map(int, open(0).read().split()))
b = copy(a)
c = copy(a)
for i in range(1, n):
    b[i] = max(b[i], b[i - 1])
for i in range(n - 2, -1, -1):
    c[i] = max(c[i], c[i + 1])
b.append(-1)
c.append(-1)
for i in range(n):
    print(max(b[i - 1], c[i + 1]))
