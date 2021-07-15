def read_nums():
    return [int(x) for x in input().split()]


def is_triangle(nums):
    for index, num in enumerate(nums):
        if nums[nums[num-1]-1] - 1 == index:
            return 'YES'
    return 'NO'


def main():
    input()
    nums = read_nums()
    print(is_triangle(nums))


def __starting_point():
    main()

__starting_point()
