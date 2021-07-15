#! /usr/bin/env python3

def main():
    input()
    nums = map(int, input().split())

    nums = sorted(nums)
    length = len(nums)
    count = 0
    last_num = nums[0]
    for i in range(length):
        if nums[i] is None:
            continue
        last_num = nums[i]
        for j in range(i + 1, length):
            if nums[j] is None:
                continue
            if nums[j] > last_num:
                count += 1
                last_num = nums[j]
                nums[j] = None

    print(count)


main()
