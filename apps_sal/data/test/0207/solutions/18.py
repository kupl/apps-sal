3


def main():
    i = int(input())
    data = [int(d) for d in input().split()]
    if data[0] % 2 + data[-1] % 2 + i % 2 < 3:
        print('No')
    else:
        print('Yes')


def __starting_point():
    main()


__starting_point()
