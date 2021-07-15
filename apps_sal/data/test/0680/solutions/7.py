xa, ya = list(map(int, input().split()))
xb, yb = list(map(int, input().split()))
xc, yc = list(map(int, input().split()))
a = [(xa, ya), (xb, yb), (xc, yc)]
a.sort()
xa = a[0][0]
xb = a[1][0]
xc = a[2][0]
ya = a[0][1]
yb = a[1][1]
yc = a[2][1]
b = []
z = []
for i in range(1050):
    b.append([0] * 1050)

b[xa][ya] = 1
b[xb][yb] = 1
b[xc][yc] = 1
for i in range(xa + 1, xb + 1):
    if b[i][ya] == 0:
        z.append((i, ya))
        b[i][ya] = 1
if yb > ya:
    for i in range(ya + 1, yb):
         if b[xb][i] == 0:
             z.append((xb, i))
             b[xb][i] = 1
else:
    for i in range(yb + 1, ya):
         if b[xb][i] == 0:
             z.append((xb, i))
             b[xb][i] = 1
for i in range(xc - 1, xb - 1, -1):
     if b[i][yc] == 0:
         z.append((i, yc))
         b[i][yc] = 1
if yc < yb:
    for i in range(yc + 1, yb):
         if b[xb][i] == 0:
             z.append((xb, i))
             b[xb][i] = 1
else:
    for i in range(yb + 1, yc):
         if b[xb][i] == 0:
             z.append((xb, i))
             b[xb][i] = 1
z.append((xa, ya))
z.append((xb, yb))
z.append((xc, yc))
print(len(z))
for i in z:
    print(i[0], i[1])

