from math import sqrt, ceil


def func(x):
    a = int(ceil(sqrt(x)))
    b = int(ceil(sqrt(2 * x)))
    for n in range(a, b + 1):
        if n == 0:
            return (1, 1)
        temp = sqrt(n ** 2 - x)
        if temp % 1 != 0 or temp == 0:
            pass
        else:
            m = int(n / temp)
            if int(n / m) == int(temp):
                return (n, m)
    return (-1, -1)


t = int(input())
for i in range(t):
    x = int(input())
    (n, m) = func(x)
    if n == -1:
        print(-1)
    else:
        print(n, m)
