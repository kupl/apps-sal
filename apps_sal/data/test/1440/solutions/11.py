N = int(input())
nums = [int(i) for i in input().split(' ')]


from collections import defaultdict


def helper(nums):
    tot, carry = 0, 0
    for i in range(len(nums)):
        v = min(nums[i]//2, carry)
        tot += v
        carry -= v
        nums[i] -= 2 * v

        tot += nums[i] // 3
        nums[i] %= 3

        carry += nums[i]
    print(tot)




helper(nums)
