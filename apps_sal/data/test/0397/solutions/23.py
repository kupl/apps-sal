import sys


def input():
    return sys.stdin.readline().strip()


def dinput():
    return int(input())


def tinput():
    return input().split()


def rinput():
    return map(int, tinput())


def rt(x1, x2, y3):
    print(0.5 * (x2 + x1) * y3)


def main():
    (n, k) = rinput()
    i = 0
    t = 0
    while k > i:
        t += 1
        i += t
    c = n - t
    i -= c
    while i != k:
        t += 1
        i += t + 1
        c -= 1
    print(c)


main()
