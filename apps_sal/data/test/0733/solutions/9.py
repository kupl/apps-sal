def test(x, y, a, b):
    t = x * y // gcd(x, y)
    return (b // t - (a - 1) // t)


def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


def main():
    s = input()
    s = list(map(int, s.split()))
    print(test(s[0], s[1], s[2], s[3]))


def __starting_point():
    main()


__starting_point()
