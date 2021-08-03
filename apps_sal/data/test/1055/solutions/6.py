# -*- coding: utf-8 -*-


def rli():
    return list(map(int, input().split()))


def solve(nums):
    if nums == sorted(nums):
        return len(nums)
    return max(solve(nums[:len(nums) // 2]), solve(nums[len(nums) // 2:]))


def main():
    input()
    nums = rli()
    print(solve(nums))


def __starting_point():
    main()


__starting_point()
