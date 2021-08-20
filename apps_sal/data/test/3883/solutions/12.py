def main():
    (a, b) = list(map(int, input().split()))
    n = a // b
    if n:
        n -= n + 1 & 1
        print('{:.12f}'.format((a + b) / (n + 1)))
    else:
        print('-1')


def __starting_point():
    main()


__starting_point()
