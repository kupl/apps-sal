from math import log


def col(n):
    rez = 0
    while n > 0:
        rez += n % 2
        n //= 2
    return rez


def f(n, p):
    for i in range(1, int(log(n, 2) + 20)):
        if col(n - p * i) == i:
            return i
        if col(n - p * i) < i and n - p * i >= i:
            return i
    return -1


n, p = list(map(int, input().split()))
print(f(n, p))
