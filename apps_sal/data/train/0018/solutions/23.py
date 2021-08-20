import math as m


def fu(a):
    return a / 180 * m.pi


t = int(input())
for _ in range(t):
    n = int(input())
    a = n // 2 - 1
    b = 180 - 360 / (2 * n)
    s = 0
    for i in range(1, a + 1):
        s = s + m.cos(fu(i * b - (2 * i - 1) * 90))
    print(2 * s + 1)
