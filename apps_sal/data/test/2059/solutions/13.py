def read_nums():
    return [int(x) for x in input().split()]


def main():
    n, = read_nums()
    nums = read_nums()
    a = [max(n - i - 1, i) for i in range(n)]
    k = min(num // val for num, val in zip(nums, a))
    print(k)


def __starting_point():
    main()


__starting_point()
