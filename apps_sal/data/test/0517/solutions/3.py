from sys import *
(n, d, h) = (int(z) for z in input().split())


def g(n, d, h):
    if d > 2 * h:
        print(-1)
        return
    if d == 1 and n > 2:
        print(-1)
        return
    if d == h:
        if n == 2:
            print(1, 2)
        else:
            for i in range(h):
                print(i + 1, i + 2)
        s = (h + 2) // 2
        for i in range(h + 2, n + 1):
            print(i, s)
        return
    for i in range(h):
        print(i + 1, i + 2)
    print(1, h + 2)
    for i in range(d - h - 1):
        print(h + 2 + i, h + 3 + i)
    for i in range(n - (d + 1)):
        print(1, d + 2 + i)


g(n, d, h)
