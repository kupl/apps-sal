n, x1, y1, x2, y2 = list(map(int, input().split()))


l = list()
for i in range(n):
    x, y = list(map(int, input().split()))
    z1 = (x - x1)**2 + (y - y1)**2
    z2 = (x - x2)**2 + (y - y2)**2
    l.append((z1, z2))

l = sorted(l, key=lambda x: x[0])

min_value = 0
for i in range(n):
    min_value = max(min_value, l[i][1])

for i in range(n):
    r1 = l[i][0]
    r2 = 0
    for j in range(i + 1, n):
        r2 = max(r2, l[j][1])
    min_value = min(min_value, r1 + r2)

print(min_value)
