def main():
    input()
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    if sum(a) >= sum(b):
        print('Yes')
    else:
        print('No')


def __starting_point():
    main()


__starting_point()
