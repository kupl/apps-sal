n, x1, y1, x2, y2 = map(int, input().split())
x = [0] * n
y = [0] * n
for i in range(n):
    x[i], y[i] = map(int, input().split())
z1, z2 = [0] * n, [0] * n
for i in range(n):
    z1[i] = (x[i] - x1)**2 + (y[i] - y1)**2
    z2[i] = (x[i] - x2)**2 + (y[i] - y2)**2
maxi = int(1e20)
for i in range(n):
    m = 0
    a1 = z1[i]
    for j in range(n):
        if j == i:
            continue
        a2 = z1[j]
        if a2 < a1:
            continue
        a2 = z2[j]
        if m < a2:
            m = a2

    if maxi > a1 + m:
        maxi = a1 + m
if maxi > max(z2):
    maxi = max(z2)
print(maxi)
