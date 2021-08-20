def main() -> int:
    n = int(input())
    if n % 2 != 0 or n < 2:
        print(-1)
    else:
        result = [i for i in range(n)]
        result[0::2] = result[2::2] + [n]
        print(' '.join((str(i) for i in result)))
    return 0


def __starting_point():
    main()


__starting_point()
