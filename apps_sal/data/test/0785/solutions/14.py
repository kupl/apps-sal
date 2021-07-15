from math import sqrt
from math import ceil

(n, a, b) = list(map(int, input().split(' ')))
batas = ceil(sqrt(6 * n))
luas = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 + \
    100
p, l = 0, 0

if a * b >= 6 * n:
    print(a * b)
    print("%d %d" % (a, b))
    return

for i in range(a, max(a, batas + 1)):
    lenmin = ceil(float(6 * n) / i)
    if lenmin < b:
        continue
    if lenmin * i == 6 * n:
        print("%d\n%d %d" % (6 * n, i, lenmin))
        return
    if lenmin * i > 6 * n:
        if lenmin * i < luas:
            p = i
            l = lenmin
            luas = lenmin * i

for i in range(b, max(b, batas + 1)):
    lenmin = ceil(float(6 * n) / i)
    if lenmin < a:
        continue
    if lenmin * i == 6 * n:
        print("%d\n%d %d" % (6 * n, lenmin, i))
        return
    if lenmin * i > 6 * n:
        if lenmin * i < luas:
            p = lenmin
            l = i
            luas = lenmin * i

print("%d\n%d %d" % (p * l, p, l))

