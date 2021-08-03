koor = dict()
a = input()
xa = int(a.split()[0])
ya = int(a.split()[1])
b = input()
xb = int(b.split()[0])
yb = int(b.split()[1])
c = input()
xc = int(c.split()[0])
yc = int(c.split()[1])
koor[ya] = xa
koor[yb] = xb
koor[yc] = xc
print(max(xa, xb, xc) + max(ya, yb, yc) - min(xa, xb, xc) - min(ya, yb, yc) + 1)
for i in range(max(xa, xb, xc) - min(xa, xb, xc) + 1):
    print(min(xa, xb, xc) + i, ya + yb + yc - min(ya, yb, yc) - max(ya, yb, yc))
for i in range(max(ya, yb, yc) - (ya + yb + yc - min(ya, yb, yc) - max(ya, yb, yc))):
    print(koor[max(ya, yb, yc)], max(ya, yb, yc) - i)
for i in range(-min(ya, yb, yc) + (ya + yb + yc - min(ya, yb, yc) - max(ya, yb, yc))):
    print(koor[min(ya, yb, yc)], min(ya, yb, yc) + i)
