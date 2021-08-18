import math
n = int(input())
tx, ty = 0, 0
x, y = [], []

for i in range(n):
    tx, ty = list(map(int, input().split()))
    x.append(tx)
    y.append(ty)


cx = 0
cy = 0
rad = 0
jud = 0
diffr = 0
maxdist = 0
sx, sy = [], []


for i in range(n - 1):
    for j in range(i + 1, n):
        if rad < math.sqrt((x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j])):
            rad = math.sqrt((x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j]))
            cx = (x[i] + x[j]) / 2
            cy = (y[i] + y[j]) / 2

if rad >= max([math.sqrt((cx - x[i]) * (cx - x[i]) + (cy - y[i]) * (cy - y[i])) for i in range(n)]) * 2:
    jud = 1

if jud == 1:
    rad = rad / 2
else:
    p, sx, sy = n, x, y
    rad = 800
    for i in range(0, p - 2):
        for j in range(i + 1, p - 1):
            for k in range(j + 1, p):
                a = sx[i]
                b = sy[i]
                c = sx[j]
                d = sy[j]
                e = sx[k]
                f = sy[k]
                aa = 2 * (c - a)
                bb = 2 * (d - b)
                cc = c * c - a * a + d * d - b * b
                dd = 2 * (e - a)
                ee = 2 * (f - b)
                ff = e * e - a * a + f * f - b * b
                z = bb * dd - aa * ee
                if z != 0:
                    cx = (bb * ff - cc * ee) / z
                    cy = (cc * dd - aa * ff) / z
                    maxdist = max([math.sqrt((cx - sx[m]) * (cx - sx[m]) + (cy - sy[m]) * (cy - sy[m])) for m in range(p)])
                    diffr = math.sqrt((cx - a) * (cx - a) + (cy - b) * (cy - b))
                    if maxdist <= diffr and diffr < rad:
                        rad = diffr

print(rad)
