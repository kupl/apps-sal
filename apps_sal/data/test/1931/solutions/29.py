import math as m


def func(a):
    return int((m.sqrt(24 * a + 1) - 1) // 6)


t = int(input())
for _ in range(t):
    n = int(input())
    c = 0
    while n > 1:
        a = func(n)
        n = n - (3 * a * a + a) // 2
        c = c + 1
    print(c)
