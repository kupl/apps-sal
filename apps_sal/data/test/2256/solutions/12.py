import random


def get_many_ints():
    return list(map(int, input().split()))


def get_int():
    return int(input())


def get_int_list():
    return list(get_many_ints())


def prog():
    n, x, a, b = get_many_ints()
    if a > b:
        a, b = b, a
    da = min(a - 1, x)
    a -= da
    x -= da
    db = min(n - b, x)
    x -= db
    b += db
    print(b - a)


q = get_int()
for _ in range(q):
    prog()
