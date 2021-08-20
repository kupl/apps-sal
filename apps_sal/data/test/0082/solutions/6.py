import math


def main():
    (n, k) = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    if sum(a) / n >= k - 0.5:
        print(0)
        return
    m = math.ceil(((k - 0.5) * n * 2 - 2 * sum(a)) / (2 * k - 2 * (k - 0.5)))
    print(int(m))


def __starting_point():
    main()


__starting_point()
