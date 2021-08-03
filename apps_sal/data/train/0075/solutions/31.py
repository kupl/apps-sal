from math import sin, cos, pi

n = int(input())


def f(a, b):
    return sin((b * pi) / a) / sin(pi / a)


for _ in range(n):
    m = int(input())
    print("%.12f" % (f(2 * m, m) * cos(pi / (4 * m))))
