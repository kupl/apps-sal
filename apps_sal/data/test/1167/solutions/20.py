from math import *
MOD = 10 ** 9 + 7


def I():
    return list(map(int, input().split()))


(t,) = I()
while t:
    t -= 1
    (a, b, c, d, k) = I()
    for i in range(k + 1):
        j = k - i
        if i * c >= a and j * d >= b:
            print(i, j)
            break
    else:
        print(-1)
