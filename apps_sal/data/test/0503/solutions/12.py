from collections import defaultdict
import time


def __starting_point():
    (n, k) = [int(x) for x in input().split()]
    nums = [int(x) for x in input().split()]
    left = [0] * len(nums)
    predict = defaultdict(int)
    for i in range(len(nums)):
        num = nums[i]
        if num % k == 0:
            left[i] = predict[num // k]
        predict[num] += 1
    right = [0] * len(nums)
    nextdict = defaultdict(int)
    for i in range(len(nums) - 1, -1, -1):
        num = nums[i]
        right[i] = nextdict[num * k]
        nextdict[num] += 1
    print(sum([left[i] * right[i] for i in range(len(nums))]))


__starting_point()
