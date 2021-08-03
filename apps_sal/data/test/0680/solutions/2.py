xa, ya = list(map(int, input().split()))
xb, yb = list(map(int, input().split()))
xc, yc = list(map(int, input().split()))

srx = xa + xb + xc - min(xa, xb, xc) - max(xa, xb, xc)
sry = ya + yb + yc - min(ya, yb, yc) - max(ya, yb, yc)

l = max(xa, xb, xc) - min(xa, xb, xc) + max(ya, yb, yc) - min(ya, yb, yc) + 1
print(l)

for i in range(min(xa, xb, xc), max(xa, xb, xc) + 1):
    print(i, sry)

if (ya != sry):
    i = ya
    while (i != sry):
        print(xa, i)
        i += int((sry - ya) / abs(sry - ya))
if (yb != sry):
    i = yb
    while (i != sry):
        print(xb, i)
        i += int((sry - yb) / abs(sry - yb))
if (yc != sry):
    i = yc
    while (i != sry):
        print(xc, i)
        i += int((sry - yc) / abs(sry - yc))
