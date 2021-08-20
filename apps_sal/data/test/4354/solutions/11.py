(n, m) = map(int, input().split())
a = [0] * n
b = [0] * n
for i in range(n):
    (a[i], b[i]) = map(int, input().split())
c = [0] * m
d = [0] * m
for j in range(m):
    (c[j], d[j]) = map(int, input().split())
for i in range(n):
    e = []
    for j in range(m):
        e.append(abs(a[i] - c[j]) + abs(b[i] - d[j]))
    f = e.index(min(e))
    print(f + 1)
