def read_nums():
    return [int(x) for x in input().split()]


def main():
    n, = read_nums()
    nums = sorted(read_nums())
    res = min(nums[-2] - nums[0], nums[-1] - nums[1])
    print(res)


def __starting_point():
    main()

__starting_point()
