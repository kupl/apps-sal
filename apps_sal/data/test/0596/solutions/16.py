t = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]


def g(y, m):
    return int(m > 2 and y % 4 == 0 and (y % 100 != 0 or y % 400 == 0))


def h(y):
    return y // 4 - y // 100 + y // 400


def f(y, m, d):
    nonlocal t
    return 365 * y + t[m] + d + h(y - 1) + g(y, m)


print(abs(f(*map(int, input().split(':'))) - f(*map(int, input().split(':')))))
