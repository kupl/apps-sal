def main():
    from itertools import product

    def f(a):
        x = int((a * 2. + .25) ** .5 + .51)
        if x * (x - 1) != a * 2:
            raise ValueError
        return (x,) if a else (1, 0)

    a00, a01, a10, a11 = list(map(int, input().split()))
    try:
        for b, w in product(f(a00), f(a11)):
            if b * w == a01 + a10:
                break
        else:
            raise ValueError
    except ValueError:
        print("Impossible")
    else:
        a01, rest = divmod(a01, w) if w else (b, 0)
        if rest:
            l = ['0' * a01, '1' * (w - rest), '0', '1' * rest, '0' * (b - a01 - 1)]
        else:
            l = ['0' * a01, '1' * w, '0' * (b - a01)]
        print(''.join(l))


def __starting_point():
    main()


__starting_point()
