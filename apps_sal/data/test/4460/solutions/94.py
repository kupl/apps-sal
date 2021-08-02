def main():
    nums = list(map(int, input().split()))
    for i, n in enumerate(nums):
        if n == 0:
            return i + 1


def __starting_point():
    print(main())


__starting_point()
