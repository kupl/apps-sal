(g, d, f) = map(int, input().split())
G = sorted([0] + list(map(int, input().split())))
D = sorted([0] + list(map(int, input().split())))
F = sorted([0] + list(map(int, input().split())))
G.append(0)
D.append(0)
F.append(0)
a = [0] * 1000000
b = [0] * 1000000
c = [0] * 1000000
x = 1
y = 1
z = 1
for i in range(1, 200001):
    if G[x] == i:
        a[i] = a[i - 1] + 1
        x += 1
    else:
        a[i] = a[i - 1]
    if D[y] == i:
        b[i] = b[i - 1] + 1
        y += 1
    else:
        b[i] = b[i - 1]
    if F[z] == i:
        c[i] = c[i - 1] + 1
        z += 1
    else:
        c[i] = c[i - 1]
q = 0
for i in range(1, 100001):
    a2 = a[2 * i] - a[i]
    b2 = b[2 * i] - b[i]
    c2 = c[2 * i] - c[i]
    if a[i] - a[i - 1] == 1:
        q += b2 * (b2 - 1) // 2 * (c2 * (c2 - 1) * (c2 - 2) // 6)
    if b[i] - b[i - 1] == 1:
        q += a2 * b2 * (c2 * (c2 - 1) * (c2 - 2) // 6)
    if c[i] - c[i - 1] == 1:
        q += a2 * (b2 * (b2 - 1) // 2) * (c2 * (c2 - 1) // 2)
print(q)
