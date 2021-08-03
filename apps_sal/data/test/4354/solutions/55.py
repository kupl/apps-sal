n, m = map(int, input().split())
a = [0] * n
b = [0] * n
c = [0] * m
d = [0] * m
for i in range(n):
    a[i], b[i] = map(int, input().split())
for i in range(m):
    c[i], d[i] = map(int, input().split())

for i in range(n):
    dist = abs(a[i] - c[0]) + abs(b[i] - d[0])
    point = 1
    for j in range(1, m):
        if dist > (abs(a[i] - c[j]) + abs(b[i] - d[j])):
            dist = (abs(a[i] - c[j]) + abs(b[i] - d[j]))
            point = j + 1
    print(point)
