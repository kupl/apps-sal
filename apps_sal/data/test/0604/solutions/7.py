def read_nums():
    return [int(x) for x in input().split()]


def main():
    n = read_nums()
    nums = read_nums()
    s = set([x for x in nums if x != 0])
    print(len(s))


def __starting_point():
    main()


__starting_point()
