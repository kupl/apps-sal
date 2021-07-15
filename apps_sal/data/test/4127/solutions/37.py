def main():
    from decimal import Decimal
    N, M = (Decimal(i) for i in input().split())
    print((int(N * M)))


def __starting_point():
    main()

__starting_point()
