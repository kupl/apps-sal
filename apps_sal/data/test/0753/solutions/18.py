import random
from fractions import gcd


def average(x):
    return sum(x) / len(x)


def shuffled(a):
    a = list(a)
    random.shuffle(a)
    return a


def read_ints():
    return [int(i) for i in input().split()]


def decrease(a):
    return [i - 1 for i in a]


def main():
    (a, b, c, d) = read_ints()
    if a / b < c / d:
        (a, b, c, d) = (b, a, d, c)
    (p, q) = (a * d - c * b, b * d)
    (s, t) = (p, a * d)
    print(s // gcd(s, t), t // gcd(s, t), sep='/')


def __starting_point():
    main()


__starting_point()
