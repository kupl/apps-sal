def main():
    (n, m) = map(int, input().split())
    res = [['.'] * m for _ in range(n + 3)]
    res[::2] = [['#'] * m for _ in range(0, n + 3, 2)]
    for l in res[1::4]:
        l[-1] = '#'
    for l in res[3::4]:
        l[0] = '#'
    for l in res[:n]:
        print(''.join(l))


def __starting_point():
    main()


__starting_point()
