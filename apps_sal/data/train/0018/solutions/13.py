from math import sin, pi

n = int(input())

def f(a, b):
    return sin((b * pi) / a) / sin(pi / a)

for _ in range(n):
    m = int(input())
    if m % 2 == 0:
        print("%.12f" % f(2 * m, m - 1))
    else:
        print("%.12f" % f(2 * m, m))

