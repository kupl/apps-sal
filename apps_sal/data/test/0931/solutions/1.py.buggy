h, w, x, y, z, p = map(int, input().split())

x %= 4
y %= 2
z %= 4


def rot(a, b):
    nonlocal h
    nonlocal w
    res = b, h - a + 1
    w, h = h, w
    return res


def flip(a, b):
    return a, w - b + 1


for i in range(p):
    a, b = map(int, input().split())
    sh, sw = h, w
    for i in range(x):
        a, b = rot(a, b)
    for i in range(y):
        a, b = flip(a, b)
    for i in range(3 * z):
        a, b = rot(a, b)
    print(a, b)
    h, w = sh, sw
