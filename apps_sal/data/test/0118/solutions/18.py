def main():
    (t, s, x) = list(map(int, input().split()))
    if (x - t >= s or x == t) and (x - t) % s in (0, 1):
        print('YES')
    else:
        print('NO')


def __starting_point():
    main()


__starting_point()
