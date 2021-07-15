from collections import Counter

def getd(n):
    v = 1
    while n > 7 ** v:
        v += 1
    return v

def getb(n, d):
    v = 0
    for i in range(d):
        b = 1 << (n % 7)
        if v & b:
            return 0
        v |= b
        n //= 7
    return v

def getc(n, d):
    c = Counter()
    for i in range(n):
        cb = getb(i, d)
        if cb:
            c[cb] += 1
    return c

x, y = map(int, input().split())
xd, yd = getd(x), getd(y)
if xd + yd > 7:
    print(0)
    return
xc, yc, v = getc(x, xd), getc(y, yd), 0
for xi in xc:
    for yi in yc:
        if xi & yi == 0:
            v += xc[xi] * yc[yi]
print(v)
