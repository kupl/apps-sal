a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())


def f(x):
    if 1 <= x and x <= 10:
        return 10
    elif 11 <= x and x <= 20:
        return 20
    elif 21 <= x and x <= 30:
        return 30
    elif 31 <= x and x <= 40:
        return 40
    elif 41 <= x and x <= 50:
        return 50
    elif 51 <= x and x <= 60:
        return 60
    elif 61 <= x and x <= 70:
        return 70
    elif 71 <= x and x <= 80:
        return 80
    elif 81 <= x and x <= 90:
        return 90
    elif 91 <= x and x <= 100:
        return 100
    elif 101 <= x and x <= 110:
        return 110
    elif 111 <= x and x <= 120:
        return 120
    else:
        return 130


aa = a + f(b) + f(c) + f(d) + f(e)
bb = b + f(c) + f(d) + f(e) + f(a)
cc = c + f(d) + f(e) + f(a) + f(b)
dd = d + f(e) + f(a) + f(b) + f(c)
ee = e + f(a) + f(b) + f(c) + f(d)
print(min(aa, bb, cc, dd, ee))
