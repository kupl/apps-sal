#!/usr/bin/pypy
# -*- coding: utf-8 -*-


def main():
    input()
    nums = sorted(map(int, input().split()))
    ft = 0
    ans = 0
    for ed in range(len(nums)):
        num = nums[ed]
        while num > nums[ft] + 5:
            ft += 1
        ans = max(ans, ed - ft + 1)
    print(ans)


def __starting_point():
    main()

__starting_point()
