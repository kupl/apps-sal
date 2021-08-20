ch = input()
d = ch.split()
h1 = int(d[0])
h2 = int(d[1])
ch = input()
d1 = ch.split()
a = int(d1[0])
b = int(d1[1])
S = 2
D = 0
if h1 < h2:
    if b > a and 8 * a < h2 - h1:
        print(-1)
    elif b == a and 8 * a < h2 - h1:
        print(-1)
    elif h1 < h2:
        if 8 * a >= h2 - h1:
            print(0)
        else:
            h1 += a * 8
            h1 -= b * 12
            D += 1
        while h1 < h2:
            if h1 + a * 12 >= h2:
                break
            h1 += (a - b) * 12
            D += 1
        if D != 0:
            print(D)
else:
    h1 + 8 * a
    if a > b and 12 * b < h1 - h2:
        print(-1)
    elif b == a and b * 12 < 8 * a + h1 - h2:
        print(-1)
    elif h1 > h2:
        if 12 * b >= h1 - h2:
            print(0)
        else:
            h2 += a * 12
            h2 -= b * 12
            D += 1
        while h1 > h2:
            if h2 - b * 12 >= h1:
                break
            h2 += (b - a) * 12
            D += 1
        if D != 0:
            print(D)
