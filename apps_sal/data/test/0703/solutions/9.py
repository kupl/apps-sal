import math


def main():
    (k, a, b, v) = [int(i) for i in input().split()]
    s = math.ceil(a / v)
    total = min(b // (k - 1), math.ceil(s / k))
    if b // (k - 1) < math.ceil(s / k):
        s -= b // (k - 1) * k
        x = 1 + b % (k - 1)
        total += 1
        if s > x:
            total += s - x
    print(total)


def __starting_point():
    main()


__starting_point()
