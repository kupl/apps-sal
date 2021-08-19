def buy_an_integer(a, b, x, l, r):
    c = (l + r) // 2
    price = a * c + b * len(str(c))
    if price > x:
        if c == r:
            return c
        return buy_an_integer(a, b, x, l, c)
    else:
        if c == l:
            return c
        return buy_an_integer(a, b, x, c, r)


def main():
    (a, b, x) = list(map(int, input().strip().split()))
    if a + b > x:
        return 0
    if a * 10 ** 9 + b * 10 < x:
        return 10 ** 9
    return buy_an_integer(a, b, x, 0, 10 ** 9)


if __name__ == '__main__':
    print(main())
