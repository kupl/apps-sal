from math import sqrt


def hex(l):
    return 1 + 3 * l * (l + 1)


def level(n):
    if n == 0:
        return (0, 0)
    l = int((-3.0 + sqrt(9.0 + 12.0 * (n - 1))) / 6.0)
    while hex(l) > n:
        l -= 1
    while hex(l + 1) <= n:
        l += 1
    return (l + 1, n - hex(l))


def coordinates(l, k):
    if l == 0:
        return (0, 0)
    (s, i) = divmod(k, l)
    if s == 0:
        return (2 * l - (i + 1), 2 * (i + 1))
    elif s == 1:
        return (l - 2 * (i + 1), 2 * l)
    elif s == 2:
        return (-l - (i + 1), 2 * l - 2 * (i + 1))
    elif s == 3:
        return (-2 * l + (i + 1), -2 * (i + 1))
    elif s == 4:
        return (-l + 2 * (i + 1), -2 * l)
    elif s == 5:
        return (l + (i + 1), -2 * l + 2 * (i + 1))


def ayrat(n):
    (l, k) = level(n)
    return coordinates(l, k)


def __starting_point():
    n = int(input())
    print('{} {}'.format(*ayrat(n)))


__starting_point()
