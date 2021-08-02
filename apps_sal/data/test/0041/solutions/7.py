def main():
    n = int(input())
    a = list(map(int, input().split()))

    zero_i = None
    f = []
    for i, ai in enumerate(a):
        if ai == 0:
            zero_i = i

        if zero_i is None:
            f.append(n)
        else:
            f.append(i - zero_i)

    zero_i = None
    b = []
    for i, ai in enumerate(reversed(a)):
        if ai == 0:
            zero_i = i

        if zero_i is None:
            b.append(n)
        else:
            b.append(i - zero_i)

    res = (min(fi, bi) for fi, bi in zip(f, reversed(b)))
    for x in res:
        print(x, end=' ')


def __starting_point():
    main()


__starting_point()
